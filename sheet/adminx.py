# -*- coding:utf-8 -*-
# @FileName  :adminx.py
# @Time      :2020-08-06 22:44
# @Author    :Alex Liu

import xadmin
from sheet.models import UserProfile,Knowledge

class KnowledgeAdmin(object):
    list_display = ['id','title','detail']
    style_fields = {
        "detail":"ueditor"
    }

xadmin.site.register(Knowledge, KnowledgeAdmin)