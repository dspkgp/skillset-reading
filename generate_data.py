from parse_data import get_role_data, get_skillset_data, get_skill_data, get_role_to_skillset_mapping
import pprint
import json

role_to_skillset_mapping = get_role_to_skillset_mapping()
role_data = get_role_data()
skillset_data = get_skillset_data()
skill_data = get_skill_data()

final_data = {}

for key, value in role_to_skillset_mapping.items():
    try:
        final_data.update({
                key : {
                    'role_description' : role_data[key]['role_description'],
                    'role_task' : role_data[key]['role_task'],
                    'possible_next_role' : role_data[key]['possible_next_role'],
                    'skillsets' : {}
                }
            })
    except:
        print key

    for key2, value2 in value.items():
        try:
            final_data[key]['skillsets'].update({key2 : {
                    'certification_url' : skillset_data[key2]['certification_url'],
                    'image_url' : skillset_data[key2]['image_url'],
                    'description' : skillset_data[key2]['description'],
                    'university' : skillset_data[key2]['university'],
                    'skills' : {}
                }})
        except:
            print key2

        for skill in value2:
            try:
                final_data[key]['skillsets'][key2]['skills'].update({skill : {
                        'video_url' : skill_data[skill]['video_url'],
                        'video_name' : skill_data[skill]['video_name'],
                        'thumbnail_url' : skill_data[skill]['thumbnail_url'],
                        'video_description' : skill_data[skill]['video_description'],
                        'video_duration' : skill_data[skill]['video_duration']
                    }})
            except:
                print skill

pprint.pprint(final_data)

jsonstring = json.dumps(final_data, indent=4, sort_keys=True)
f = open("database.py", "w")
f.write(jsonstring)
f.close()
