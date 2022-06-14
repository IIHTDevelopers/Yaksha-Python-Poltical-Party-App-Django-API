
from rest_framework.test import APITestCase
from partyapp.models import PoliticalPartyModel,PoliticalLeaderModel,DevelopmentModel
from partyapp.test.TestUtils import TestUtils
class PoliticalAPIFunctionalTest(APITestCase):
    # @classmethod
    # def setUpTestData(cls):
    #     PoliticalPartyModel.objects.create(
    #     party_id= 1,
    #     party_name= "TDP",
    #     party_founder= "NTR")
    #
    #     PoliticalLeaderModel.objects.create(
    #     leader_id= 1,
    #     party_id=1,
    #     candidate_name="Naidu",
    #     state_name="Telangana"
    #     )
    #
    #     DevelopmentModel.objects.create(
    #     development_id= 1,
    #     leader_id= 1,
    #     development_title= "Mission Bhagiratha",
    #     development_activity= "Free Water Supply Throughout State",
    #     development_budget=450.00,
    #     development_state= "TS",
    #     development_activity_month= 11,
    #     development_activity_year= 2015)
    #
    #     with open("../output_revised.txt","w") as f:
    #         pass

    def test_fetch_all_registered_political_parties(self):
        test_obj = TestUtils()
        url='http://127.0.0.1:8000/politicalparty/'
        response=self.client.get(url)
        if response.status_code==200:
            test_obj.yakshaAssert("TestFetchAllRegisteredPoliticalParties", True, "functional")
            print("TestFetchAllRegisteredPoliticalParties=Passed")
        else:
            test_obj.yakshaAssert("TestFetchAllRegisteredPoliticalParties", False, "functional")
            print("TestFetchAllRegisteredPoliticalParties=Failed")

    def test_get_political_party_by_id(self):
        test_obj = TestUtils()
        url='http://127.0.0.1:8000/politicalparty_pk/1/'
        response=self.client.get(url)
        if response.status_code==200:
            test_obj.yakshaAssert("TestGetPoliticalPartyById", True, "functional")
            print("TestGetPoliticalPartyById=Passed")
        else:
            test_obj.yakshaAssert("TestGetPoliticalPartyById", False, "functional")
            print("TestGetPoliticalPartyById=Failed")

    def test_register_political_party(self):
        test_obj = TestUtils()
        url='http://127.0.0.1:8000/politicalparty/'
        data={
        "party_id": 1,
        "party_name": "TDP",
        "party_founder": "NTR"
        }
        response=self.client.post(url,data,format='json')
        if response.status_code==201:
            test_obj.yakshaAssert("TestGetPoliticalPartyById", True, "functional")
            print("TestGetPoliticalPartyById=Passed")
        else:
            test_obj.yakshaAssert("TestGetPoliticalPartyById", False, "functional")
            print("TestGetPoliticalPartyById=Failed")

    def test_update_political_party(self):
        test_obj = TestUtils()
        url='http://127.0.0.1:8000/politicalparty_pk/1/'
        data={
        # "party_id": 1,
        # "party_name": "TDP",
        "party_founder": "RamaRao"
        }
        response=self.client.patch(url,data,format='json')
        if response.status_code==200:
            test_obj.yakshaAssert("TestUpdatePoliticalParty", True, "functional")
            print("TestUpdatePoliticalParty=Passed")
        else:
            test_obj.yakshaAssert("TestUpdatePoliticalParty", False, "functional")
            print("TestUpdatePoliticalParty=Failed")

    def test_delete_political_party(self):
        test_obj = TestUtils()
        url='http://127.0.0.1:8000/politicalparty_pk/1/'
        response=self.client.delete(url)
        if response.status_code==200:
            test_obj.yakshaAssert("TestDeletePoliticalParty", True, "functional")
            print("TestDeletePoliticalParty=Passed")
        else:
            test_obj.yakshaAssert("TestDeletePoliticalParty", False, "functional")
            print("TestDeletePoliticalParty=Failed")

#PoliticalLeader

    def test_fetch_all_registered_political_leaders(self):
        test_obj = TestUtils()
        url='http://127.0.0.1:8000/politicalleader/'
        response=self.client.get(url)
        if response.status_code==200:
            test_obj.yakshaAssert("TestFetchAllRegisteredPoliticalLeaders", True, "functional")
            print("TestFetchAllRegisteredPoliticalLeaders=Passed")
        else:
            test_obj.yakshaAssert("TestFetchAllRegisteredPoliticalLeaders", False, "functional")
            print("TestFetchAllRegisteredPoliticalLeaders=Failed")

    def test_get_political_leader_by_id(self):
        test_obj = TestUtils()
        url='http://127.0.0.1:8000/politicalleader_pk/1/'
        response=self.client.get(url)
        if response.status_code==200:
            test_obj.yakshaAssert("TestGetPoliticalLeaderById", True, "functional")
            print("TestGetPoliticalLeaderById=Passed")
        else:
            test_obj.yakshaAssert("TestGetPoliticalLeaderById", False, "functional")
            print("TestGetPoliticalLeaderById=Failed")

    def test_register_political_leader(self):
        test_obj = TestUtils()
        url='http://127.0.0.1:8000/politicalleader/'
        data={
            "leader_id": 1,
            "party_id": 1,
            "candidate_name": "Naidu",
            "state_name": "Telangana"
        }
        response=self.client.post(url,data,format='json')
        if response.status_code==201:
            test_obj.yakshaAssert("TestRegisterPoliticalLeader", True, "functional")
            print("TestRegisterPoliticalLeader=Passed")
        else:
            test_obj.yakshaAssert("TestRegisterPoliticalLeader", False, "functional")
            print("TestRegisterPoliticalLeader=Failed")

    def test_update_political_leader(self):
        test_obj = TestUtils()
        url='http://127.0.0.1:8000/politicalleader_pk/1/'
        data={
            "leader_id": 1,
            "party_id": 1,
            "candidate_name": "C Babu Naidu",
            "state_name": "AP"
        }
        response=self.client.patch(url,data,format='json')
        if response.status_code==200:
            test_obj.yakshaAssert("TestUpdatePoliticalLeader", True, "functional")
            print("TestUpdatePoliticalLeader= Passed")
        else:
            test_obj.yakshaAssert("TestUpdatePoliticalLeader", False, "functional")
            print("TestUpdatePoliticalLeader=Failed")

    def test_delete_political_leader(self):
        test_obj = TestUtils()
        url='http://127.0.0.1:8000/politicalleader_pk/1/'
        response=self.client.delete(url)
        if response.status_code==200:
            test_obj.yakshaAssert("TestDeletePoliticalLeader", True, "functional")
            print("TestDeletePoliticalLeader=Passed")
        else:
            test_obj.yakshaAssert("TestDeletePoliticalLeaderd", False, "functional")
            print("TestDeletePoliticalLeader=Failed")

    def test_get_political_leader_by_party_id(self):
        test_obj = TestUtils()
        url='http://127.0.0.1:8000/politicalleaderbyparty/?party_id=1'
        response=self.client.get(url)
        if response.status_code==200:
            test_obj.yakshaAssert("TestGetPoliticalLeaderByPartyId", True, "functional")
            print("TestGetPoliticalLeaderByPartyId=Passed")
        else:
            test_obj.yakshaAssert("TestGetPoliticalLeaderByPartyId", False, "functional")
            print("TestGetPoliticalLeaderByPartyId=Failed")

#Development

    def test_fetch_all_created_developments(self):
        test_obj = TestUtils()
        url='http://127.0.0.1:8000/development/'
        response=self.client.get(url)
        if response.status_code==200:
            test_obj.yakshaAssert("TestFetchAllCreatedDevelopments", True, "functional")
            print("TestFetchAllCreatedDevelopments = Passed")
        else:
            test_obj.yakshaAssert("TestIsCandidateQualified", False, "functional")
            print("TestFetchAllCreatedDevelopments = Failed")

    def test_get_development_by_id(self):
        test_obj = TestUtils()
        url='http://127.0.0.1:8000/development_pk/1/'
        response=self.client.get(url)
        if response.status_code==200:
            test_obj.yakshaAssert("TestGetDevelopmentById", True, "functional")
            print("TestGetDevelopmentById = Passed")
        else:
            test_obj.yakshaAssert("TestGetDevelopmentById", False, "functional")
            print("TestGetDevelopmentById = Failed")

    def test_create_development(self):
        test_obj = TestUtils()
        url='http://127.0.0.1:8000/development/'
        data={
        "development_id": 1,
        "leader_id": 1,
        "development_title": "Mission Bhagiratha",
        "development_activity": "Free Water Supply Throughout State",
        "development_budget": "450.00",
        "development_state": "TS",
        "development_activity_month": 11,
        "development_activity_year": 2015
        }
        response=self.client.post(url,data,format='json')
        if response.status_code==201:
            test_obj.yakshaAssert("TestCreateDevelopment", True, "functional")
            print("TestCreateDevelopment = Passed")
        else:
            test_obj.yakshaAssert("TestCreateDevelopment", False, "functional")
            print("TestCreateDevelopment = Failed")

    def test_update_development(self):
        test_obj = TestUtils()
        url='http://127.0.0.1:8000/development_pk/1/'
        data={
        "development_id": 1,
        "leader_id": 1,
        "development_title": "Mission Bhagiratha",
        "development_activity": "Free Water Supply Throughout State",
        "development_budget": "450.00",
        "development_state": "TS",
        "development_activity_month": 11,
        "development_activity_year": 2015
        }
        response=self.client.patch(url,data,format='json')
        if response.status_code==200:
            test_obj.yakshaAssert("TestUpdateDevelopment", True, "functional")
            print("TestUpdateDevelopment = Passed")
        else:
            test_obj.yakshaAssert("TestUpdateDevelopment", False, "functional")
            print("TestUpdateDevelopment = Failed")

    def test_delete_development(self):
        test_obj = TestUtils()
        url='http://127.0.0.1:8000/development_pk/1/'
        response=self.client.delete(url)
        if response.status_code==200:
            test_obj.yakshaAssert("TestDeleteDevelopment", True, "functional")
            print("TestDeleteDevelopment = Passed")
        else:
            test_obj.yakshaAssert("TestDeleteDevelopment", False, "functional")
            print("TestDeleteDevelopment = Failed")

    def test_get_all_developments_by_leader_id(self):
        test_obj = TestUtils()
        url='http://127.0.0.1:8000/developmentbyleader/?leader_id=1'
        response=self.client.get(url)
        if response.status_code==200:
            test_obj.yakshaAssert("TestGetAllDevelopmentsByLeaderId", True, "functional")
            print("TestGetAllDevelopmentsByLeaderId = Passed")
        else:
            test_obj.yakshaAssert("TestGetAllDevelopmentsByLeaderId", False, "functional")
            print("TestGetAllDevelopmentsByLeaderId = Failed")
