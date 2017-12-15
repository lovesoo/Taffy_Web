# coding:utf-8

from flask_wtf import Form
from wtforms import StringField, PasswordField, IntegerField, SubmitField, BooleanField
from wtforms.widgets.core import PasswordInput
from wtforms.validators import DataRequired, Email, NumberRange


class PasswordField(PasswordField):
    # 修改PasswordInput参数值显示密码
    widget = PasswordInput(hide_value=False)


class configForm(Form):
    taffy_dir = StringField(u"项目路径", description=u"不建议使用中文", validators=[DataRequired()])
    report_name = StringField(u"测试报告前缀", validators=[DataRequired()])
    auto_send = BooleanField(u"是否自动发送报告邮件")
    mail_host = StringField(u"邮件服务器地址", validators=[DataRequired()])
    mail_port = IntegerField(u"邮件服务器端口", validators=[DataRequired(), NumberRange(0, 65535)])
    mail_user = StringField(u"发件人地址", validators=[DataRequired(), Email()])
    mail_pwd = PasswordField(u"发件人密码/授权码", validators=[DataRequired()])
    mail_subject = StringField(u"邮件标题前缀", validators=[DataRequired()])
    mail_to = StringField(u"收件人地址", description=u'多个地址请以;分割', validators=[DataRequired()])
    submit_button = SubmitField(u"保存修改")
