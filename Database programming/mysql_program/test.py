#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/5/21 14:12
# @Author  : ChenYao
# @File    : test.py
import sqlalchemy
from sqlalchemy import Column, String
from sqlalchemy.dialects.mysql import TINYINT, INTEGER, VARCHAR, DATETIME
from sqlalchemy.ext.declarative import declarative_base

engine = sqlalchemy.create_engine("mysql://root:meidi@192.168.163.83/news?charset=utf8")
Base = declarative_base()


class User(Base):
    __tablename__ = 'users'
    uid = Column(INTEGER(unsigned=True), nullable=False, primary_key=True)
    nickname = Column(VARCHAR(65), nullable=True)
    avatar = Column(VARCHAR(255), nullable=True)
    status = Column(TINYINT(2), nullable=True, default=0)
    gender = Column(TINYINT(2), nullable=True, default=1)
    uright = Column(VARCHAR(255), nullable=True, default="")


class Account(Base):
    __tablename__ = 'account'
    uid = Column(INTEGER(10, unsigned=True), nullable=False, primary_key=True)
    account = Column(VARCHAR(50), nullable=False, default="")
    pwd = Column(VARCHAR(255), nullable=False, default="")


class UserInfo(Base):
    __tablename__ = 'users_info'
    uid = Column(INTEGER, nullable=False, primary_key=True)
    email = Column(VARCHAR(50), default="")
    qq = Column(VARCHAR(25), default="")
    mobile = Column(VARCHAR(25), default="")


class UserFollow(Base):
    __tablename__ = 'user_follow'
    id = Column(INTEGER(11, unsigned=True), nullable=False, primary_key=True)
    uid = Column(INTEGER(11, unsigned=True), nullable=False, default=0)
    anchor = Column(INTEGER(11, unsigned=True), nullable=False, default=0)
    status = Column(TINYINT(3, unsigned=True), nullable=False, default=1)
    isAnchor = Column(TINYINT(3, unsigned=True), nullable=False, default=1)
    isFriends = Column(TINYINT(4), nullable=False, default=0)
    dateline = Column(INTEGER(11, unsigned=True), nullable=False, default=0)
    befriendsAt = Column(INTEGER(10, unsigned=True), nullable=False, default=0)
    fansCnt = Column(INTEGER(11, unsigned=True), nullable=False, default=0)
    anchorFansCnt = Column(INTEGER(11, unsigned=True), nullable=False, default=0)


class SignAnchor(Base):
    __tablename__ = 'sign_anchor'
    id = Column(INTEGER(11, unsigned=True), nullable=False, primary_key=True)
    uid = Column(INTEGER(11, unsigned=True), nullable=False, default=None)
    cellphone = Column(VARCHAR(32), default=None)
    qq = Column(VARCHAR(20), default=None)
    gameId = Column(TINYINT(11, unsigned=True), default=None)
    realname = Column(VARCHAR(64), nullable=False, default=None)
    gender = Column(TINYINT(1, unsigned=True), nullable=False, default=2)
    province = Column(VARCHAR(64), default=None)
    city = Column(VARCHAR(64), default=None)
    liveTime = Column(VARCHAR(1024), default=None)
    isAbroad = Column(TINYINT(4, unsigned=True), default=0)
    cpu = Column(VARCHAR(64), default=None)
    broadband = Column(VARCHAR(64), default=None)
    idcardNum = Column(VARCHAR(64), nullable=False, default=0)
    idcardFront = Column(VARCHAR(255), default=None)
    idcardBack = Column(VARCHAR(255), default=None)
    idcardBg = Column(VARCHAR(255), default=None)
    liveRoom1 = Column(VARCHAR(255), default=None)
    liveRoom2 = Column(VARCHAR(255), default=None)
    liveRoom3 = Column(VARCHAR(255), default=None)
    bankcardNum = Column(VARCHAR(64), default=None)
    bankcardAddress = Column(VARCHAR(255), default=None)
    bankName = Column(VARCHAR(64), default=None)
    bankBranchName = Column(VARCHAR(255), default=None)
    status = Column(TINYINT(1), nullable=False, default=0)
    verifyStatus = Column(TINYINT(1), default=0)
    reason = Column(VARCHAR(512), default=None)
    source = Column(TINYINT(4), default=1)
    ip = Column(VARCHAR(32), default=None)
    createTime = Column(INTEGER(11, unsigned=True), nullable=False)

User.metadata.create_all(engine)