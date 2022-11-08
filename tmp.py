# ###########################  settings   ###########################################################
import os
import shutil
from datetime import datetime, time, timedelta

from airflow.models import DAG
from airflow.models.variable import Variable
from airflow.operators.bash_operator import BashOperator
from airflow.operators.python_operator import PythonOperator
from bigdataservice2.bigdataservice.da.model import DataVersion, UserDataSource
from bigdataservice2.bigdataservice.da.session import get_transient_session
from bigdataservice2.bigdataservice.settings import (DAILY_DATA_PATH,
                                                     DAY_FORMAT,
                                                     SQLALCHEMY_DATABASE_URI)
from bigdataservice2.bigdataservice.utils import generate_version
from bigdataservice2.bigdataservice.utils.log import log
from bigdatasource.impl.bigdatasource import DataSource

# 临时导出数据使用 bigdataservice_export_data_tmp

DATA_EXPIRED_DAYS = 2  # 数据版本 过期时间，超过这个日期的数据将被删除
DAY_FORMAT = "%Y-%m-%d"

start_date = datetime.now().strftime(DAY_FORMAT)
end_date = start_date
# start_date='2022-08-29'
# end_date ='2022-08-30'


DATA_PATH = "/var/app/data/bigquant/datasource/daily"


wecom_key = "b4a29147-2933-4362-904c-4ae2b9cb6983"

# 提醒的人  古涛 / 张明禄 / 于永平
wecom_mentioned_list = ["18502808368", "15680272518", "13551726910"]

# ###########################  settings   ###########################################################

from airflow.utils.trigger_rule import TriggerRule  # noqa

trigger_rule = TriggerRule.ALL_DONE


def sleep(seconds):
    import time
    time.sleep(seconds)


args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2019, 11, 22),
    'wecom_key': wecom_key,
    'wecom_mentioned_list': wecom_mentioned_list,
    'retries': 5,
    'retry_delay': timedelta(minutes=1),
    'email_on_failure': True,
    'email_on_retry': False
}

dag = DAG(
    'export_data_tob',
    schedule_interval=None,
    catchup=False,
    default_args=args,
    tags=['bigquant'],
    description="将B端客户需要的数据每天导出, bigdataservice2 提供下载数据服务"
)

# #######################################   导出数据，转化为py36版本可读取    ############################################################

# ###########################  settings   ###########################################################

# 临时导出数据使用 bigdataservice_export_data_tmp

DATASOURCE_ID_LIST = []  # 表名列表  只在需要为某个用户导出特定表数据是使用一次

DATA_EXPIRED_DAYS = 7  # 数据版本 过期时间，超过这个日期的数据将被删除


SQLALCHEMY_ECHO = False  # 是否打印sql

# ###########################  settings   ###########################################################


def get_user_datasource_list(session, user_name=None):
    if user_name:
        db_query = session.query(UserDataSource.datasource_id).filter(
            UserDataSource.user_name == user_name)
    else:
        db_query = session.query(UserDataSource.datasource_id)
    return [i[0] for i in db_query.distinct().all()]


with get_transient_session(SQLALCHEMY_DATABASE_URI, echo=False) as session:
    latest_version = session.query(DataVersion). \
        filter(DataVersion.is_active.is_(True)). \
        filter(DataVersion.owner.in_(["all"])). \
        order_by(DataVersion.create_time.desc()).first()
    version = latest_version.version if latest_version else ""
