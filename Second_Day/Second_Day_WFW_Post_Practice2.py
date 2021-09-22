from flask import Flask,jsonify,request,make_response

app = Flask(__name__)

IPL ={
    "RCB" : {
             "Devdatt_Padikal": 17,
             "Virat_Kohali": 18,
             "Team_Devid":55,
             "Max_Vell": 32,
            "ABDevelears": 17,
            "Whashinton_Sunder":55,
            "Kile_Jeminson":34,
            "harshal_patel":65,
            "navdeep_saine":34,
            "mohamad_seraj":43,
            "uzevendra_chahal":34,
            },
    "RR" : {
             "Even_leves ": 63,
             "Manan_vohara ": 55,
             "Sanju_Samsung": 22,
             "Shivam_Dube" :33,
             "Glen_fhilips" :33,
             "Devid_Milar ": 56,
             "Riyan_parag" :34,
             "Rahul_tevatiya ":67,
             "cris_moris" :33,
             "jaydev_vunadkut" :23,
             "kartik_tyagi":36,

            },
    "DC" : {
             "Shikar_Dhavan ": 63,
             "Prithwi_Show" : 23,
             "Shreyas_iyar" : 34,
             "Rushab_Pant ": 55,
             "simron_hetmayer": 22,
              "marcus_stoinis" : 76,
             "Aksher_patel": 68,
              "Amit_mishra" : 47,
              "Kagiso_rabada":48,
              "Arnek_norjeya":38,
              "Avesh_khan":38,
            }
}