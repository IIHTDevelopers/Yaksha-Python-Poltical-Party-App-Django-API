from rest_framework.test import APITestCase
from partyapp.models import PoliticalPartyModel,PoliticalLeaderModel,DevelopmentModel
from partyapp.test.TestUtils import TestUtils
class PoliticalAPIExceptionalTest(APITestCase):
    @classmethod
    def setUpTestData(cls):
        PoliticalPartyModel.objects.create(
        party_id= 1,
        party_name= "TDP",
        party_founder= "NTR")
    
        PoliticalLeaderModel.objects.create(
        leader_id= 1,
        party_id=1,
        candidate_name="Naidu",
        state_name="Telangana"
        )
    
        DevelopmentModel.objects.create(
        development_id= 1,
        leader_id= 1,
        development_title= "Mission Bhagiratha",
        development_activity= "Free Water Supply Throughout State",
        development_budget=450.00,
        development_state= "TS",
        development_activity_month= 11,
        development_activity_year= 2015)
    
        with open("../output_revised.txt","w") as f:
            pass

    def test_fetch_all_registered_political_parties_fail(self):
        test_obj = TestUtils()
        url='http://127.0.0.1:8000/politicalpartyx/'
        response=self.client.get(url)
        if response.status_code==404:
            test_obj.yakshaAssert("TestFetchAllRegisteredPoliticalPartiesFail", True, "exception")
            print("TestFetchAllRegisteredPoliticalPartiesFail = Passed")
        else:
            test_obj.yakshaAssert("TestFetchAllRegisteredPoliticalPartiesFail", False, "exception")
            print("TestFetchAllRegisteredPoliticalPartiesFail = Failed")

    def test_get_political_party_by_non_exist_id(self):
        test_obj = TestUtils()
        url='http://127.0.0.1:8000/politicalparty_pk/111/'
        response=self.client.get(url)
        if response.status_code==500:
            test_obj.yakshaAssert("TestGetPoliticalPartyByNonExistId", True, "exception")
            print("TestGetPoliticalPartyByNonExistId = Passed")
        else:
            test_obj.yakshaAssert("TestGetPoliticalPartyByNonExistId", False, "exception")
            print("TestGetPoliticalPartyByNonExistId= Failed")

    def test_register_political_party_with_insufficient_data(self):
        test_obj = TestUtils()
        url='http://127.0.0.1:8000/politicalparty/'
        data={
        "party_id": 1,
        "party_name": "TDP"
        }
        response=self.client.post(url,data,format='json')
        if response.status_code==500:
            test_obj.yakshaAssert("TestRegisterPoliticalPartyWithInsufficientData", True, "exception")
            print("TestRegisterPoliticalPartyWithInsufficientData = Passed")
        else:
            test_obj.yakshaAssert("TestRegisterPoliticalPartyWithInsufficientData", False, "exception")
            print("TestRegisterPoliticalPartyWithInsufficientData= Failed")

    def test_update_political_party_by_non_exist_id(self):
        test_obj = TestUtils()
        url='http://127.0.0.1:8000/politicalparty_pk/1111/'
        data={
        "party_founder": "RamaRao"
        }
        response=self.client.patch(url,data,format='json')
        if response.status_code==500:
            test_obj.yakshaAssert("TestUpdatePoliticalPartyByNonExistId", True, "exception")
            print("TestUpdatePoliticalPartyByNonExistId = Passed")
        else:
            test_obj.yakshaAssert("TestUpdatePoliticalPartyByNonExistId", False, "exception")
            print("TestUpdatePoliticalPartyByNonExistId = Failed")

    def test_delete_political_party_by_non_exist_id(self):
        test_obj = TestUtils()
        url='http://127.0.0.1:8000/politicalparty_pk/1111/'
        response=self.client.delete(url)
        if response.status_code==500:
            test_obj.yakshaAssert("TestDeletePoliticalPartyByNonExistId", True, "exception")
            print("TestDeletePoliticalPartyByNonExistId = Passed")
        else:
            test_obj.yakshaAssert("TestDeletePoliticalPartyByNonExistId", False, "exception")
            print("TestDeletePoliticalPartyByNonExistId = Failed")

#PoliticalLeader

    def test_fetch_all_registered_political_leaders_fail(self):
        test_obj = TestUtils()
        url='http://127.0.0.1:8000/politicalleaderx/'
        response=self.client.get(url)
        if response.status_code==404:
            test_obj.yakshaAssert("TestFetchAllRegisteredPoliticalLeadersFail", True, "exception")
            print("TestFetchAllRegisteredPoliticalLeadersFail = Passed")
        else:
            test_obj.yakshaAssert("TestFetchAllRegisteredPoliticalLeadersFail", False, "exception")
            print("TestFetchAllRegisteredPoliticalLeadersFail = Failed")

    def test_get_political_leader_by_non_exist_id(self):
        test_obj = TestUtils()
        url='http://127.0.0.1:8000/politicalleader_pk/111/'
        response=self.client.get(url)
        if response.status_code==500:
            test_obj.yakshaAssert("TestGetPoliticalLeaderByNonExistId", True, "exception")
            print("TestGetPoliticalLeaderByNonExistId = Passed")
        else:
            test_obj.yakshaAssert("TestGetPoliticalLeaderByNonExistId", False, "exception")
            print("TestGetPoliticalLeaderByNonExistId = Failed")

    def test_register_political_leader_with_insufficient_data(self):
        test_obj = TestUtils()
        url='http://127.0.0.1:8000/politicalleader/'
        data={
            "leader_id": 1,
            "party_id": 1,
            "candidate_name": "Naidu",
        }
        response=self.client.post(url,data,format='json')
        if response.status_code==500:
            test_obj.yakshaAssert("TestRegisterPoliticalLeaderWithInsufficientData", True, "exception")
            print("TestRegisterPoliticalLeaderWithInsufficientData = Passed")
        else:
            test_obj.yakshaAssert("TestRegisterPoliticalLeaderWithInsufficientData", False, "exception")
            print("TestRegisterPoliticalLeaderWithInsufficientData = Failed")

    def test_update_political_leader_by_non_exist_id(self):
        test_obj = TestUtils()
        url='http://127.0.0.1:8000/politicalleader_pk/111/'
        data={
            "leader_id": 1,
            "party_id": 1,
            "candidate_name": "C Babu Naidu",
            "state_name": "AP"
        }
        response=self.client.patch(url,data,format='json')
        if response.status_code==500:
            test_obj.yakshaAssert("TestUpdatePoliticalLeaderByNonExistId", True, "exception")
            print("TestUpdatePoliticalLeaderByNonExistId = Passed")
        else:
            test_obj.yakshaAssert("TestUpdatePoliticalLeaderByNonExistId", False, "exception")
            print("TestUpdatePoliticalLeaderByNonExistId = Failed")

    def test_delete_political_leader_by_non_exist_id(self):
        test_obj = TestUtils()
        url='http://127.0.0.1:8000/politicalleader_pk/1111/'
        response=self.client.delete(url)
        if response.status_code==500:
            test_obj.yakshaAssert("TestDeletePoliticalLeaderByNonExistId", True, "exception")
            print("TestDeletePoliticalLeaderByNonExistId = Passed")
        else:
            test_obj.yakshaAssert("TestDeletePoliticalLeaderByNonExistId", False, "exception")
            print("TestDeletePoliticalLeaderByNonExistId = Failed")

    def test_get_political_leader__by_non_exist_party_id(self):
        test_obj = TestUtils()
        url='http://127.0.0.1:8000/politicalleaderbyparty/?party_id=111'
        response=self.client.get(url)
        if response.status_code==500:
            test_obj.yakshaAssert("TestGetPoliticalLeaderByNonExistPartyId", True, "exception")
            print("TestGetPoliticalLeaderByNonExistPartyId = Passed")
        else:
            test_obj.yakshaAssert("TestGetPoliticalLeaderByNonExistPartyId", False, "exception")
            print("TestGetPoliticalLeaderByNonExistPartyId = Failed")

#Development

    def test_fetch_all_created_developments_fail(self):
        test_obj = TestUtils()
        url='http://127.0.0.1:8000/developmentx/'
        response=self.client.get(url)
        if response.status_code==404:
            test_obj.yakshaAssert("TestFetchAllCreatedDevelopmentsFail", True, "exception")
            print("TestFetchAllCreatedDevelopmentsFail = Passed")
        else:
            test_obj.yakshaAssert("TestFetchAllCreatedDevelopmentsFail", False, "exception")
            print("TestFetchAllCreatedDevelopmentsFail = Failed")

    def test_get_development_by_non_exist_id(self):
        test_obj = TestUtils()
        url='http://127.0.0.1:8000/development_pk/111/'
        response=self.client.get(url)
        if response.status_code==500:
            test_obj.yakshaAssert("TestGetDevelopmentByNonExistId", True, "exception")
            print("TestGetDevelopmentByNonExistId = Passed")
        else:
            test_obj.yakshaAssert("TestGetDevelopmentByNonExistId", False, "exception")
            print("TestGetDevelopmentByNonExistId = Failed")

    def test_create_development_fail_with_insufficient_data(self):
        test_obj = TestUtils()
        url='http://127.0.0.1:8000/developmentx/'
        data={
        "development_id": 1,
        "leader_id": 1,
        "development_title": "Mission Bhagiratha",
        "development_activity": "Free Water Supply Throughout State",
        "development_budget": "450.00",
        "development_state": "TS",
        }
        response=self.client.post(url,data,format='json')
        if response.status_code==404:
            test_obj.yakshaAssert("TestCreateDevelopmentFailWithInsufficientData", True, "exception")
            print("TestCreateDevelopmentFailWithInsufficientData = Passed")
        else:
            test_obj.yakshaAssert("TestCreateDevelopmentFailWithInsufficientData", False, "exception")
            print("TestCreateDevelopmentFailWithInsufficientData = Failed")

    def test_update_development_by_non_exist_id(self):
        test_obj = TestUtils()
        url='http://127.0.0.1:8000/development_pk/111/'
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
        if response.status_code==500:
            test_obj.yakshaAssert("TestUpdateDevelopmentByNonExistId", True, "exception")
            print("TestUpdateDevelopmentByNonExistId = Passed")
        else:
            test_obj.yakshaAssert("TestUpdateDevelopmentByNonExistId", False, "exception")
            print("TestUpdateDevelopmentByNonExistId = Failed")


    def test_delete_development_by_non_exist_id(self):
        test_obj = TestUtils()
        url='http://127.0.0.1:8000/development_pk/1111/'
        response=self.client.delete(url)
        if response.status_code==500:
            test_obj.yakshaAssert("TestDeleteDevelopmentByNonExistId", True, "exception")
            print("TestDeleteDevelopmentByNonExistId = Passed")
        else:
            test_obj.yakshaAssert("TestDeleteDevelopmentByNonExistId", False, "exception")
            print("TestDeleteDevelopmentByNonExistId = Failed")

    def test_get_all_developments_by_non_exist_leader_id(self):
        test_obj = TestUtils()
        url='http://127.0.0.1:8000/developmentbyleader/?leader_id=111'
        response=self.client.get(url)
        if response.status_code==500:
            test_obj.yakshaAssert("TestGetAllDevelopmentsByNonExistLeaderId", True, "exception")
            print("TestGetAllDevelopmentsByNonExistLeaderId = Passed")
        else:
            test_obj.yakshaAssert("TestGetAllDevelopmentsByNonExistLeaderId", False, "exception")
            print("TestGetAllDevelopmentsByNonExistLeaderId = Failed")
