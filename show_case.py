#!/usr/bin/env python
# -*- coding: utf-8 -*-
#coding=utf-8
import logging
from PyMysqlPool.db_util.mysql_util import query, insertOrUpdate

from FlaskPoolShowcase.mysql_config import db_config


def flask_query():
    job_status = 2
    _sql = "select *  from master_job_list j  where j.job_status  !=%s "
    _args = (job_status,)
    task = query(db_config['local'], _sql,_args)
    logging.info("query_npool method query_npool result is %s ,input _data is %s ", task , _args)

def flask_insertOrUpdate(nlp_rank_id,hit_query_word):
    #add more args
    _args = (nlp_rank_id,hit_query_word)
    _sql = """INSERT INTO nlp_rank_poi_online (nlp_rank_id,hit_query_word,rank_type,poi_list,poi_raw_list,article_id,city_id,status,create_time,version,source_from) VALUES (%s,%s,%s, %s, %s,%s, %s,%s, %s,%s,%s)"""
    affect = insertOrUpdate(db_config['local'], _sql, _args)
    logging.info("insert method insert result is %s ,input _data is %s ", affect , _args)


if __name__ == "__main__":
    flask_query()