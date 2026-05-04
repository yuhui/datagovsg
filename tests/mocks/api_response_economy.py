# Copyright 2026 Yuhui
#
# Licensed under the GNU General Public License, Version 3.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.gnu.org/licenses/gpl-3.0.html
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# pylint: disable=line-too-long,missing-class-docstring,missing-function-docstring

"""Mock response for the Economy module."""

class APIResponseDesigns:
    status_code = 200

    @staticmethod
    def json():
        return {
            "lodgement_date": "2020-01-20",
            "count": 2,
            "items": [
                {
                    "license": None,
                    "applicantsRightsWithRespectToDesign": "By Virtue of Employment",
                    "applicationNum": "30202007578S",
                    "applicant": [
                        {
                            "address": "777 Old Saw Mill River Road<br/>Tarrytown, NY 10591<br/>USA ",
                            "articles": [
                                {
                                    "articleName": "PACKAGING",
                                    "numOfArticlesInSet": 0
                                }
                            ],
                            "countryofIncorporationOrResidence": {
                                "code": "US",
                                "description": "United States of America"
                            },
                            "name": "Regeneron Pharmaceuticals, Inc.",
                            "nationality": {
                                "code": None,
                                "description": None
                            },
                            "soleProprietorPartnerName": None,
                            "stateOfIncorporation": {
                                "code": "NY",
                                "description": "New York"
                            },
                            "uenCompanyCode": "E00309044T"
                        }
                    ],
                    "hmgStatus": None,
                    "priorityDetails": [
                        {
                            "associatedDesignNum": None,
                            "country": "United States of America",
                            "priorityClaimsDate": "2019-07-29"
                        }
                    ],
                    "transferOfOwnership": None,
                    "summary": {
                        "applicationNum": "30202007578S",
                        "approvedDate": "2020-01-29",
                        "classSubClass": "09-05",
                        "expiryDate": "2035-01-20",
                        "filingDate": "2020-01-20",
                        "internationalRegistrationDate": None,
                        "internationalRegistrationNum": None,
                        "lodgementDate": "2020-01-20",
                        "renewalDueDate": "2025-01-20",
                        "status": "Registered",
                        "ukDesignNum": None,
                        "ukRegistrationDate": None
                    },
                    "agentCorrespondenceDetails": [
                        {
                            "actionRepresenting": "For all matters relating to the application, registration/grant, except those matters expressly excluded ",
                            "addressForServiceinSingapore": "77 ROBINSON ROAD<br/>#22-01 ROBINSON 77<br/>Singapore 068896",
                            "agent": {
                                "name": "AMICA LAW LLC",
                                "uenCompanyCode": "200601697N"
                            },
                            "representationType": "Agent",
                            "representativeOrCOName": None
                        }
                    ],
                    "securityInterest": None,
                    "disclaimer": "The broken / stippled lines are for illustrative purposes only and form no part of the claimed design.<br />The shaded portions are for illustrative purposes only and form no part of the claimed design.<br />",
                    "otherEntries": [
                        {
                            "events": {
                                "code": "RD024",
                                "description": "DESIGN PUBLISHED IN 02/2020 ",
                                "eventDate": "2020-02-07"
                            }
                        }
                    ],
                    "journals": [
                        {
                            "journalDate": "2020-02-07",
                            "journalNum": "02/2020"
                        }
                    ],
                    "statementOfNovelty": "Novelty resides in the Shape and Configuration as shown in the Representation(s).",
                    "documents": [
                        {
                            "docType": {
                                "code": "RDIMG",
                                "description": "Images"
                            },
                            "fileId": "CEC262A4-8C98-4BA8-AB6F-52B91DFD20C8",
                            "fileName": "cec262a4-8c98-4ba8-ab6f-52b91dfd20c8.jpg",
                            "lodgementDate": "2020-01-20",
                            "url": "https://ipos-storage.data.gov.sg/designs/30202007578S/34c4ff67-e878-48f4-8321-f74e501c971e/cec262a4-8c98-4ba8-ab6f-52b91dfd20c8.jpg"
                        }
                    ],
                    "currentApplicantProprietorDetails": [
                        {
                            "applicantType": {
                                "code": "C",
                                "description": "Corporate"
                            }
                        }
                    ]
                },
                {
                    "statementsOfGrantOfProtection": None,
                    "renunciations": None,
                    "nameAndAddressOfTheCreatorOfTheDesign": "1-41: Simon VAN ANKEN, Curacaostraat 101-H, 1058BS, Amsterdam, NL; 1-41: Peter GAL, Balistraat 25/3, 1094JB, Amsterdam, NL; 1-41: Lieven ADRIAENSSEN, Olmstraat 83k, 1800, Vilvoorde, BE; 1-41: Roel KROOSHOF, Bosuillaan 279, 3722XM, Bilthoven, NL; 1-41: Jos ",
                    "documents": [
                        {
                            "docType": {
                                "code": "RDIMG",
                                "description": "Images"
                            },
                            "fileId": "2456C4F5-ADB2-4E4A-BB1C-476C21CBCC05",
                            "fileName": "2456c4f5-adb2-4e4a-bb1c-476c21cbcc05.jpg",
                            "lodgementDate": "2020-07-29",
                            "url": "https://ipos-storage.data.gov.sg/designs/D208452/d16a1951-a7d5-4686-a6dd-e98905189c02/2456c4f5-adb2-4e4a-bb1c-476c21cbcc05.jpg"
                        }
                    ],
                    "applicationNum": "D208452",
                    "changesInNameAddressOfTheHolder": None,
                    "fusionMergersOfInternationalRegistrations": None,
                    "invalidations": None,
                    "renewals": None,
                    "stateInWhichOwnerHasARealAndEffectiveIndustrialOrCommercialEstablishment": "European Union",
                    "limitations": None,
                    "refusals": None,
                    "changesinOwnership": None,
                    "summary": {
                        "WIPOPublicationDate": "2020-07-24",
                        "agent": {
                            "address": "High Tech Campus 5, 5656 AE Eindhoven, NL, Eindhoven, 5656 AE",
                            "name": "Philips Intellectual Property &amp; Standards"
                        },
                        "applicant": {
                            "address": "High Tech Campus 5, 5656 AE EindhovenEindhovenNL",
                            "name": "Koninklijke Philips N.V."
                        },
                        "applicantsContractingParty": "European Union",
                        "bulletinNum": "30/2020",
                        "country": "Benelux, European Union",
                        "designatedStates": "Turkey, Ukraine, United Kingdom, Singapore, Russian Federation",
                        "designationofArticle": "1.-6. Shaver; 7.-11. Handle for shaver; 12. Shaver; 13.-16. Handle for shaver; 17.-20. Head for shaver; 21.-26. Cutting unit for shaver; 27.-31. Head for shaver; 32.-33. Cutting unit for shaver; 34.-35. Head for shaver; 36.-39. Shaver; 40.-43. Lighting ring for shaver",
                        "expectedExpiryRenewalDate": "2025-01-20",
                        "internationalFilingDate": "2020-01-20",
                        "internationalRegistrationNum": "D208452",
                        "locarnoClassSubClass": "28-03",
                        "numberofDesigns": 43,
                        "priorityCountry": "European Union",
                        "priorityDate": "2019-08-06",
                        "status": "Approved"
                    }
                }
            ]
        }

class APIResponsePatents:
    status_code = 200

    @staticmethod
    def json():
        return {
            "lodgement_date": "2020-01-20",
            "count": 1,
            "items": [
                {
                    "pctApplication": None,
                    "rupka": [
                        {
                            "xGazetteDate": None,
                            "xGazetteNum": None,
                            "xIsSection261c": None,
                            "xPatentNum": None,
                            "xukGrantDate": None,
                            "xukNum": None
                        }
                    ],
                    "applicationNum": "10202000492Q",
                    "otherEntries": [
                        {
                            "events": {
                                "code": "PT003",
                                "description": "FE CLEAR REPORT ISSUED",
                                "eventDate": "2020-03-26"
                            }
                        }
                    ],
                    "declarationOfPriority": [
                        {
                            "applicationNum": "10-2017-0060940",
                            "country": {
                                "code": "KR",
                                "description": "Republic of Korea"
                            },
                            "filingDate": "2017-05-17"
                        }
                    ],
                    "inventors": [
                        {
                            "address": "(Munpyeongdong) 8-26, Munpyeongseo-ro,<br/>Daedeok-gu, Daejeon 34302<br/>",
                            "countryOfResidence": {
                                "code": "KR",
                                "description": "Republic of Korea"
                            },
                            "name": "BAN, Eun Hye",
                            "nationality": "KOREAN, SOUTH"
                        }
                    ],
                    "securityInterest": None,
                    "divisionalApplications": None,
                    "documents": [
                        {
                            "docType": {
                                "code": "ACLMO",
                                "description": "Amendment of Claim(s) only"
                            },
                            "fileId": "B2536047-E633-48D4-B6FA-613EB662F8BA",
                            "fileName": "b2536047-e633-48d4-b6fa-613eb662f8ba.pdf",
                            "lodgementDate": "2020-03-03",
                            "url": "https://ipos-storage.data.gov.sg/patents/10202000492Q/9e16b04a-86da-4517-829e-8fd109241a8b/b2536047-e633-48d4-b6fa-613eb662f8ba.pdf"
                        }
                    ],
                    "transferOfOwnership": None,
                    "currentApplicantProprietorDetails": [
                        {
                            "applicantType": {
                                "code": "C",
                                "description": "Corporate"
                            }
                        }
                    ],
                    "hmgStatus": None,
                    "grantAndRenewal": {
                        "dateOfGrantOfUKEUPatentNum": None,
                        "dateOfIssueOfCertificateOfRegistrationInSingapore": None,
                        "dateOfLastRenewal": None,
                        "dateOfRenewal": None,
                        "divisionalParentOfUKEUPatentNum": None,
                        "expiryDate": None,
                        "grantDate": None,
                        "nextRenewalDate": None,
                        "yearOfLastRenewal": None
                    },
                    "agentCorrespondenceDetails": [
                        {
                            "actionRepresenting": "For all matters relating to the application, registration/grant, except those matters expressly excluded ",
                            "addressForServiceInSingapore": "10 COLLYER QUAY<br/>#10-01 OCEAN FINANCIAL CENTRE<br/>Singapore 049315",
                            "agent": {
                                "name": "DREW & NAPIER LLC",
                                "uenCompanyCode": "200102509E"
                            },
                            "representationType": "Agent",
                            "representativeName": None
                        }
                    ],
                    "license": None,
                    "summary": {
                        "applicationNum": "10202000492Q",
                        "applicationStatus": "Pending (Published)",
                        "applicationType": "Divisional",
                        "dateOfPublication": "2020-03-30",
                        "filingDate": "2018-05-15",
                        "ipc": None,
                        "lodgementDate": "2020-01-20",
                        "publicationPatentNumForOldApplication": None,
                        "titleOfInvention": "NOVEL COMPOUNDS AS AUTOTAXIN INHIBITORS AND PHARMACEUTICAL COMPOSITIONS COMPRISING THE SAME"
                    },
                    "applicant": [
                        {
                            "address": "(Munpyeongdong) 8-26, Munpyeongseo-ro,<br/>Daedeok-gu, Daejeon 34302<br/>REPUBLIC OF KOREA ",
                            "countryOfIncorporationOrResidence": {
                                "code": "KR",
                                "description": "Republic of Korea"
                            },
                            "name": "LEGOCHEM BIOSCIENCES, INC.",
                            "nationality": {
                                "code": None,
                                "description": None
                            },
                            "soleProprietorPartnerName": None,
                            "stateOfIncorporation": {
                                "code": None,
                                "description": None
                            },
                            "uenCompanyCode": "E18023411Q"
                        }
                    ]
                }
            ]
        }

class APIResponseTrademarks:
    status_code = 200

    @staticmethod
    def json():
        return {
            "lodgement_date": "2020-01-20",
            "count": 1,
            "items": [
                {
                    "transferOfOwnership": None,
                    "replacementApplicationMadridBy": None,
                    "license": None,
                    "markIndex": [
                        {
                            "chineseCharacter": None,
                            "descrOfDevice": "duck face",
                            "enTranslation": None,
                            "enTransliteration": None,
                            "phoneticEquiv": None,
                            "wordsInMark": "IRVINS SALTED EGG"
                        }
                    ],
                    "internationalApplicationDetails": None,
                    "markClauses": None,
                    "transformationApplicationMadridFrom": None,
                    "documents": [
                        {
                            "docType": {
                                "code": "MarkLogo",
                                "description": "Trade Mark Logo"
                            },
                            "fileId": "0DBBB962-F5D8-4CC1-E37E-79452BC639CF",
                            "fileName": "0dbbb962-f5d8-4cc1-e37e-79452bc639cf.tif",
                            "lodgementDate": "2020-01-20",
                            "url": "https://ipos-storage.data.gov.sg/trademarks/40202001321Q/149f4ce9-f367-4599-82ff-d21c499e9df8/0dbbb962-f5d8-4cc1-e37e-79452bc639cf.tif"
                        }
                    ],
                    "priorityClaimsDetails": None,
                    "logogramArticle6TerDetails": None,
                    "transformationApplicationMadridInto": None,
                    "goodsAndServicesSpecifications": [
                        {
                            "classExpiryDate": None,
                            "classNum": "Class 16",
                            "classStatus": {
                                "code": "PUE",
                                "description": "Pending (Under Examination)"
                            },
                            "goodsServices": "Printed matter; Newsletters; Magazines [periodicals]; Pictures; Calendars; Cards; Greeting cards; Posters; Photographs; Gift wrapping paper; Memo pads; Booklets; Bookmarkers; Coasters of paper; Place mats of paper; Note books; Memorandum books; Picture cards; Post cards; Bumper stickers; Paper napkins; Menus."
                        }
                    ],
                    "summary": {
                        "applicationDate": "2020-01-20",
                        "applicationNum": "40202001321Q",
                        "applicationType": "Trade Mark",
                        "descriptionParticularFeatureOfMark": None,
                        "disclaimerLimitation": None,
                        "expiryDate": None,
                        "filingDate": "2020-01-20",
                        "internationalRegDate": None,
                        "journals": None,
                        "markStatus": "Pending (Under Examination)",
                        "markStatusDate": "2020-01-20",
                        "publicationDate": None,
                        "registrationProcedureCompletionDate": None,
                        "seriesMarkNum": 0,
                        "singaporeProtectionDate": "2020-01-20",
                        "statusUpdateDate": "2020-01-20",
                        "tradeMarkType": "Conventional Mark"
                    },
                    "currentApplicantProprietorDetails": [
                        {
                            "address": "61 TREVOSE CRESCENT<br/>DUNEARN ESTATE<br/>Singapore 298062",
                            "applicantType": {
                                "code": "C",
                                "description": "Corporate"
                            },
                            "countryOfIncorporationOrResidence": {
                                "code": "SG",
                                "description": "Singapore"
                            },
                            "name": "COCOBA PTE. LTD.",
                            "nationality": {
                                "code": None,
                                "description": None
                            },
                            "soleProprietorPartnerName": None,
                            "stateOfIncorporation": {
                                "code": None,
                                "description": None
                            },
                            "uenCompanyCode": "200702419E"
                        }
                    ],
                    "agentCorrespondenceDetails": [
                        {
                            "actionRepresenting": "For all matters relating to the application, registration/grant, except those matters expressly excluded ",
                            "addressForServiceinSingapore": "200 CANTONMENT ROAD<br/>#14-03 SOUTHPOINT<br/>Singapore 089763",
                            "agent": {
                                "name": None,
                                "uenCompanyCode": None
                            },
                            "representationType": "Non-Agent",
                            "representativeName": None
                        }
                    ],
                    "internationlRegistrationDesignatingSingaporeDetails": None,
                    "otherEntries": None,
                    "securityInterest": None,
                    "HMGcases": None,
                    "applicationNum": "40202001321Q",
                    "replacementApplicationMadridReplaces": None
                }
            ]
        }

__all__ = [
    'APIResponseDesigns',
    'APIResponsePatents',
    'APIResponseTrademarks',
]
