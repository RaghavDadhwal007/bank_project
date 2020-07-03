from rest_framework import serializers
from .models import Branches, Bank


class BankSerializer(serializers.ModelSerializer):

    class Meta:
        model = Bank
        fields = ["Name", ]


class BranchSerializer(serializers.ModelSerializer):

    class Meta:
        model = Branches
        fields = ["ifsc", "branch", "address", "city", "district", "state"]
