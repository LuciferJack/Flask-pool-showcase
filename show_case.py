#!/usr/bin/env python
# -*- coding: utf-8 -*-
#coding=utf-8
from PyMysqlPool.db_util.db_config.mysql_config import db_config
from PyMysqlPool.db_util.mysql_util import query


def flask_quer():
    job_status = 2
    _sql = "select *  from master_job_list j  where j.job_status  !=%s "
    _args = (job_status,)
    task = query(db_config['local'], _sql,_args)
    logging.info("query_npool method query_npool result is %s ,input _data is %s ", task , _args)

if __name__ == "__main__":