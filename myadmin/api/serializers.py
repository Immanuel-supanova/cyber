from typing import Any, Dict
from django.contrib.admin.models import LogEntry
from rest_framework import serializers

from myadmin.query import LogApp, LogAppDate, LogAppMonth, LogAppYear, LogDate, LogModel, LogModelDate, LogModelMonth, LogModelYear, LogMonth, LogUser, LogUserDate, LogUserMonth, LogUserYear, LogYear


class LogSerializer(serializers.ModelSerializer):

    class Meta:
        model = LogEntry
        fields = '__all__'


class LogYearSerializers(serializers.Serializer):
    year = serializers.CharField(max_length=128, min_length=8, write_only=True, required=True)

    def validate(self, data) -> Dict[Any, Any]:
        logs = LogYear(year=data["year"])

        
        return {
            "list":logs.yearly_list(), 
            "count":logs.yearly_count(),
            "add_list":logs.addition_yearly_list(),
            "add_count":logs.addition_yearly_count(),
            "change_list":logs.change_yearly_list(),
            "change_count":logs.change_yearly_count(),
            "del_list":logs.deletion_yearly_list(),
            "del_count":logs.deletion_yearly_count(),
            }


class LogMonthSerializers(serializers.Serializer):
    year = serializers.CharField(max_length=128, min_length=8, write_only=True, required=True)
    month = serializers.CharField(max_length=128, min_length=8, write_only=True, required=True)

    def validate(self, data) -> Dict[Any, Any]:
        logs = LogMonth(year=data["year"], month=data["month"])

        
        return {
            "list":logs.monthly_list(), 
            "count":logs.monthly_count(),
            "add_list":logs.addition_monthly_list(),
            "add_count":logs.addition_monthly_count(),
            "change_list":logs.change_monthly_list(),
            "change_count":logs.change_monthly_count(),
            "del_list":logs.deletion_monthly_list(),
            "del_count":logs.deletion_monthly_count(),
            }


class LogDateSerializers(serializers.Serializer):
    date = serializers.CharField(max_length=128, min_length=8, write_only=True, required=True)

    def validate(self, data) -> Dict[Any, Any]:
        logs = LogDate(date=data["date"])

        
        return {
            "list":logs.date_list(), 
            "count":logs.date_count(),
            "add_list":logs.addition_date_list(),
            "add_count":logs.addition_date_count(),
            "change_list":logs.change_date_list(),
            "change_count":logs.change_date_count(),
            "del_list":logs.deletion_date_list(),
            "del_count":logs.deletion_date_count(),
            }


class LogAppSerializers(serializers.Serializer):
    app = serializers.CharField(max_length=128, min_length=8, write_only=True, required=True)

    def validate(self, data) -> Dict[Any, Any]:
        logs = LogApp(app=data["app"])

        
        return {
            "list":logs.app_list(), 
            "count":logs.app_count(),
            }


class LogAppYearSerializers(serializers.Serializer):
    app = serializers.CharField(max_length=128, min_length=8, write_only=True, required=True)
    year = serializers.CharField(max_length=128, min_length=8, write_only=True, required=True)
    
    def validate(self, data) -> Dict[Any, Any]:
        logs = LogAppYear(app=data["app"], year=data["year"])

        
        return {
            "list":logs.yearly_list(), 
            "count":logs.yearly_count(),
            "add_list":logs.addition_yearly_list(),
            "add_count":logs.addition_yearly_count(),
            "change_list":logs.change_yearly_list(),
            "change_count":logs.change_yearly_count(),
            "del_list":logs.deletion_yearly_list(),
            "del_count":logs.deletion_yearly_count(),
            }


class LogAppMonthSerializers(serializers.Serializer):
    app = serializers.CharField(max_length=128, min_length=8, write_only=True, required=True)
    year = serializers.CharField(max_length=128, min_length=8, write_only=True, required=True)
    month = serializers.CharField(max_length=128, min_length=8, write_only=True, required=True)

    def validate(self, data) -> Dict[Any, Any]:
        logs = LogAppMonth(app=data["app"], year=data["year"], month=data["month"])

        
        return {
            "list":logs.monthly_list(), 
            "count":logs.monthly_count(),
            "add_list":logs.addition_monthly_list(),
            "add_count":logs.addition_monthly_count(),
            "change_list":logs.change_monthly_list(),
            "change_count":logs.change_monthly_count(),
            "del_list":logs.deletion_monthly_list(),
            "del_count":logs.deletion_monthly_count(),
            }


class LogAppDateSerializers(serializers.Serializer):
    app = serializers.CharField(max_length=128, min_length=8, write_only=True, required=True)
    date = serializers.CharField(max_length=128, min_length=8, write_only=True, required=True)
    
    def validate(self, data) -> Dict[Any, Any]:
        logs = LogAppDate(app=data["app"], date=data["date"])

        
        return {
            "list":logs.date_list(), 
            "count":logs.date_count(),
            "add_list":logs.addition_date_list(),
            "add_count":logs.addition_date_count(),
            "change_list":logs.change_date_list(),
            "change_count":logs.change_date_count(),
            "del_list":logs.deletion_date_list(),
            "del_count":logs.deletion_date_count(),
            }


class LogModelSerializers(serializers.Serializer):
    app = serializers.CharField(max_length=128, min_length=8, write_only=True, required=True)
    model = serializers.CharField(max_length=128, min_length=8, write_only=True, required=True)
    
    def validate(self, data) -> Dict[Any, Any]:
        logs = LogModel(app=data["app"], model=data["model"])

        return {
            "list":logs.model_list(), 
            "count":logs.model_count(),
            }
    

class LogModelYearSerializers(serializers.Serializer):
    year = serializers.CharField(max_length=128, min_length=8, write_only=True, required=True)
    app = serializers.CharField(max_length=128, min_length=8, write_only=True, required=True)
    model = serializers.CharField(max_length=128, min_length=8, write_only=True, required=True)

    def validate(self, data) -> Dict[Any, Any]:
        logs = LogModelYear(app=data["app"], year=data["year"], model=data["model"])

        return {
            "list":logs.yearly_list(), 
            "count":logs.yearly_count(),
            "add_list":logs.addition_yearly_list(),
            "add_count":logs.addition_yearly_count(),
            "change_list":logs.change_yearly_list(),
            "change_count":logs.change_yearly_count(),
            "del_list":logs.deletion_yearly_list(),
            "del_count":logs.deletion_yearly_count(),
            }


class LogModelMonthSerializers(serializers.Serializer):
    year = serializers.CharField(max_length=128, min_length=8, write_only=True, required=True)
    app = serializers.CharField(max_length=128, min_length=8, write_only=True, required=True)
    model = serializers.CharField(max_length=128, min_length=8, write_only=True, required=True)
    month = serializers.CharField(max_length=128, min_length=8, write_only=True, required=True)

    def validate(self, data) -> Dict[Any, Any]:
        logs = LogModelMonth(app=data["app"], year=data["year"], model=data["model"], month=data["month"])

        return {
            "list":logs.monthly_list(), 
            "count":logs.monthly_count(),
            "add_list":logs.addition_monthly_list(),
            "add_count":logs.addition_monthly_count(),
            "change_list":logs.change_monthly_list(),
            "change_count":logs.change_monthly_count(),
            "del_list":logs.deletion_monthly_list(),
            "del_count":logs.deletion_monthly_count(),
            }
    

class LogModelDateSerializers(serializers.Serializer):
    date = serializers.CharField(max_length=128, min_length=8, write_only=True, required=True)
    app = serializers.CharField(max_length=128, min_length=8, write_only=True, required=True)
    model = serializers.CharField(max_length=128, min_length=8, write_only=True, required=True)

    def validate(self, data) -> Dict[Any, Any]:
        logs = LogModelDate(app=data["app"], date=data["date"], model=data["model"])

        return {
            "list":logs.date_list(), 
            "count":logs.date_count(),
            "add_list":logs.addition_date_list(),
            "add_count":logs.addition_date_count(),
            "change_list":logs.change_date_list(),
            "change_count":logs.change_date_count(),
            "del_list":logs.deletion_date_list(),
            "del_count":logs.deletion_date_count(),
            }
    

class LogUserSerializers(serializers.Serializer):
    app = serializers.CharField(max_length=128, min_length=8, write_only=True, required=True)
    user = serializers.CharField(max_length=128, min_length=8, write_only=True, required=True)
    
    def validate(self, data) -> Dict[Any, Any]:
        logs = LogUser(app=data["app"], user=data["user"])

        return {
            "list":logs.user_list(), 
            "count":logs.user_count(),
            }
    

class LogUserYearSerializers(serializers.Serializer):
    year = serializers.CharField(max_length=128, min_length=8, write_only=True, required=True)
    user = serializers.CharField(max_length=128, min_length=8, write_only=True, required=True)

    def validate(self, data) -> Dict[Any, Any]:
        logs = LogUserYear(user=data["user"], year=data["year"])

        return {
            "list":logs.yearly_list(), 
            "count":logs.yearly_count(),
            "add_list":logs.addition_yearly_list(),
            "add_count":logs.addition_yearly_count(),
            "change_list":logs.change_yearly_list(),
            "change_count":logs.change_yearly_count(),
            "del_list":logs.deletion_yearly_list(),
            "del_count":logs.deletion_yearly_count(),
            }


class LogUserMonthSerializers(serializers.Serializer):
    year = serializers.CharField(max_length=128, min_length=8, write_only=True, required=True)
    user = serializers.CharField(max_length=128, min_length=8, write_only=True, required=True)
    month = serializers.CharField(max_length=128, min_length=8, write_only=True, required=True)

    def validate(self, data) -> Dict[Any, Any]:
        logs = LogUserMonth(user=data["user"], year=data["year"], month=data["month"])

        return {
            "list":logs.monthly_list(), 
            "count":logs.monthly_count(),
            "add_list":logs.addition_monthly_list(),
            "add_count":logs.addition_monthly_count(),
            "change_list":logs.change_monthly_list(),
            "change_count":logs.change_monthly_count(),
            "del_list":logs.deletion_monthly_list(),
            "del_count":logs.deletion_monthly_count(),
            }
    

class LogUserDateSerializers(serializers.Serializer):
    date = serializers.CharField(max_length=128, min_length=8, write_only=True, required=True)
    user = serializers.CharField(max_length=128, min_length=8, write_only=True, required=True)

    def validate(self, data) -> Dict[Any, Any]:
        logs = LogUserDate(user=data["user"], date=data["date"])

        return {
            "list":logs.date_list(), 
            "count":logs.date_count(),
            "add_list":logs.addition_date_list(),
            "add_count":logs.addition_date_count(),
            "change_list":logs.change_date_list(),
            "change_count":logs.change_date_count(),
            "del_list":logs.deletion_date_list(),
            "del_count":logs.deletion_date_count(),
            } 
