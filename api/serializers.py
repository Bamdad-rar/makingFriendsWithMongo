from rest_framework import serializers
from datetime import datetime, time


class reportSerializer(serializers.Serializer):
    start_date = serializers.DateTimeField(required=True)
    end_date = serializers.DateTimeField(required=True)
    start_time = serializers.TimeField(required=True, allow_null=True)
    end_time = serializers.TimeField(required=True, allow_null=True)
    name = serializers.CharField(required=False, allow_blank=True, allow_null=True)

    def validate_name(self, value):
        if (value is not None) and (not value.isalpha()):
            raise serializers.ValidationError("name is not alphabetical!")
        return value

    def getQueryDict(self):
        # get required data
        start_date = self.data["start_date"]
        end_date = self.data["end_date"]
        start_time = self.data["start_time"]
        end_time = self.data["end_time"]
        name = self.data["name"]

        # if time is available combine it with datetime field
        if start_time:
            start_time = datetime.strptime(start_time, "%H:%M:%S")
            start_time = start_time.time()
            # in order to combine, we need to make an object out of the datetime
            start_date = datetime.strptime(start_date, "%Y-%m-%dT%H:%M:%SZ")
            start_signup = datetime.combine(start_date, start_time).isoformat()
        else:
            start_signup = datetime.strptime(
                start_date, "%Y-%m-%dT%H:%M:%SZ"
            ).isoformat()

        if end_time:
            end_time = datetime.strptime(end_time, "%H:%M:%S")
            end_time = end_time.time()
            end_date = datetime.strptime(end_date, "%Y-%m-%dT%H:%M:%SZ")
            end_signup = datetime.combine(end_date, end_time).isoformat()
        else:
            end_signup = datetime.strptime(end_date, "%Y-%m-%dT%H:%M:%SZ").isoformat()

        if name:
            targetQuery = {
                "signup": {"$gte": start_signup, "$lt": end_signup},
                "name": name,
            }
        else:
            targetQuery = {"signup": {"$gte": start_signup, "$lt": end_signup}}
        return targetQuery


def clean_report(value):
    temp = value
    if temp["start_time"] == "":
        temp["start_time"] = None
    if temp["end_time"] == "":
        temp["end_time"] = None
    if temp["name"] == "":
        temp["name"] = None
    return temp
