from django.http import HttpResponse
from models.job_offer import JobOffer
import json
from parse_rest.connection import register
from parse_rest.datatypes import Object

__author__ = 'Edie'

import json, requests

jobOffersBaseURL = 'http://jobs.github.com/positions.json'

class ApiLoader(object):
    """
        This middleware allows connecting and pulling live ads data from Job Offers API.
    """
    #def initialize(self,token=None, token_secret=None):

    register('SBYaU2xzhVsjHmMAp7lxytxjF5HPJLuA0AJ2p34N', 'sS6u1bt81sHnyyJaqt7EmcJwsDqVHAaUokX7x2ou', master_key=None)

    # Load Job Offers
    def load_offers(self):
        params = dict(
        )

        resp = requests.get(url=jobOffersBaseURL, params=params)
        data = json.loads(resp.text)
        offers_list = []

        for offer in data:
            id = offer['id']
            title = offer['title']
            description = offer['description']
            compnay_url = offer['company_url']
            compnay_logo = offer['company_logo']
            created_at = offer['created_at']
            company = offer['company']
            how_to_apply = offer['how_to_apply']
            location = offer['location']
            url = offer['url']
            type = offer['type']

            row_as_dict = {
                'id' : id,
                'title' : title,
                'description': description,
                'compnay_url' : compnay_url,
                'compnay_logo' : compnay_logo,
                'created_at' : created_at,
                'company' : company,
                'how_to_apply' : how_to_apply,
                'location' : location,
                'url' : url,
                'type' : type
            }

            existing_offer = JobOfferParse.Query.all().filter(id=id)
            print len(existing_offer)
            if(len(existing_offer) == 0):
                job_offer = JobOffer.create(id,title,description,compnay_url,compnay_logo,created_at,company,how_to_apply,location,url,type)
                json_job_offer = job_offer.to_JSON()

                jobOfferParse = JobOfferParse(id=id, title=title,description=description,compnay_url= compnay_url, compnay_logo=compnay_logo, created_at= created_at,company=company,how_to_apply=how_to_apply,location=location,url=url,type=type)
                jobOfferParse.save()

            offers_list.append(row_as_dict)

        return offers_list

    def retrieve_offers(self):
        offers_list = []
        all_offers = JobOfferParse.Query.all()
        for offer in all_offers:
            id = offer.id
            title = offer.title
            description = offer.description
            compnay_url = offer.compnay_url
            compnay_logo = offer.compnay_logo
            created_at = offer.created_at
            company = offer.company
            how_to_apply = offer.how_to_apply
            location = offer.location
            url = offer.url
            type = offer.type

            job_offer = JobOffer.create(id,title,description,compnay_url,compnay_logo,created_at,company,how_to_apply,location,url,type)
            json_job_offer = job_offer.to_JSON()

            row_as_dict = {
                'id' : id,
                'title' : title,
                'description': description,
                'compnay_url' : compnay_url,
                'compnay_logo' : compnay_logo,
                'created_at' : created_at,
                'company' : company,
                'how_to_apply' : how_to_apply,
                'location' : location,
                'url' : url,
                'type' : type
            }

            offers_list.append(row_as_dict)

            print offer.title
        return offers_list

    def annotate_offer(self,text):
        offers_list = []

        dbPediaBaseURL = 'http://spotlight.sztaki.hu:2222/rest/annotate?text='+text+'&confidence=0.2&support=20'

        respond = requests.get(url=dbPediaBaseURL,headers={"Accept":"application/json"})

        data = json.loads(respond.text)

        annotations_list = []

        resources = data['Resources']

        for resource in resources:

            support = resource['@support']
            uri = resource['@URI']
            surface_form = resource['@surfaceForm']
            offset = resource['@offset']
            percentage_of_second_rank = resource['@percentageOfSecondRank']
            similarity_score = resource['@similarityScore']
            types = resource['@types']

            row_as_dict = {
                    'support' : support,
                    'uri' : uri,
                    'surface_form': surface_form,
                    'offset' : offset,
                    'percentage_of_second_rank' : percentage_of_second_rank,
                    'similarity_score': similarity_score,
                    'types': types
                }

            annotations_list.append(row_as_dict)

        return annotations_list

    def filter_offers(self,company,location,position):
        offers_list = []

        offers = JobOfferParse.Query.all()

        print offers

        if((company != 'all') & (location != 'all') & (position != 'all')):
             offers = JobOfferParse.Query.all().filter(company=company).filter(location=location).filter(title=position)
        elif((company == 'all') & (location != 'all') & (position != 'all')):
             offers = JobOfferParse.Query.all().filter(location=location).filter(title=position)
        elif((company != 'all') & (location == 'all') & (position != 'all')):
             offers = JobOfferParse.Query.all().filter(company=company).filter(title=position)
        elif((company != 'all') & (location != 'all') & (position == 'all')):
             offers = JobOfferParse.Query.all().filter(company=company).filter(location=location)
        elif((company == 'all') & (location == 'all') & (position != 'all')):
             offers = JobOfferParse.Query.all().filter(title=position)
        elif((company == 'all') & (location != 'all') & (position == 'all')):
             offers = JobOfferParse.Query.all().filter(location=location)
        elif((company != 'all') & (location == 'all') & (position == 'all')):
             offers = JobOfferParse.Query.all().filter(company=company)
        elif((company == 'all') & (location == 'all') & (position != 'all')):
             offers = JobOfferParse.Query.all().filter(title=position)
        elif((company == 'all') & (location == 'all') & (position == 'all')):
             offers = JobOfferParse.Query.all()

        print offers
        for offer in offers:
            id = offer.id
            title = offer.title
            description = offer.description
            compnay_url = offer.compnay_url
            compnay_logo = offer.compnay_logo
            created_at = offer.created_at
            company = offer.company
            how_to_apply = offer.how_to_apply
            location = offer.location
            url = offer.url
            type = offer.type

            job_offer = JobOffer.create(id,title,description,compnay_url,compnay_logo,created_at,company,how_to_apply,location,url,type)
            json_job_offer = job_offer.to_JSON()

            row_as_dict = {
                'id' : id,
                'title' : title,
                'description': description,
                'compnay_url' : compnay_url,
                'compnay_logo' : compnay_logo,
                'created_at' : created_at,
                'company' : company,
                'how_to_apply' : how_to_apply,
                'location' : location,
                'url' : url,
                'type' : type
            }

            offers_list.append(row_as_dict)

        return offers_list


class JobOfferParse(Object):
    pass