import pprint


from parse_data import get_role_data, get_skillset_data, get_skill_data, get_role_to_skillset_mapping


SPACE_COUNTER = 10

def get_same_value_outputs(input_skill_level, output_skill_level):
    if output_skill_level == 'HIGH' and input_skill_level == 'LOW':
        return ['MEDIUM', 'HIGH']
    elif output_skill_level == 'HIGH' and input_skill_level == "MEDIUM":
        return ['HIGH']
    elif output_skill_level == 'MEDIUM' and input_skill_level == 'LOW':
        return ['MEDIUM']
    elif output_skill_level == input_skill_level:
        return []
    else:
        return []


def get_single_value_outputs(output_skill_level):
    if output_skill_level == 'HIGH':
        return ['LOW', 'MEDIUM', 'HIGH']

    elif output_skill_level == 'MEDIUM':
        return ['LOW', 'MEDIUM']

    else:
        return ['LOW']


def get_role_gap(input_role, output_role, role_to_skillset_mapping):
    import ipdb; ipdb.set_trace()
    input_skillset = role_to_skillset_mapping[input_role]
    output_skillset = role_to_skillset_mapping[output_role]

    print "\n"

    output_skillset_keys = output_skillset.keys()
    input_skillset_keys = input_skillset.keys()
    final_skillset = {}

    for key, value in output_skillset.items():
        final_skillset.update({key : []})

        if input_skillset.has_key(key):
            for output_skill in value:
                input_skill_level_mapping = {}
                input_skills = input_skillset[key]
                output_skill_name = output_skill.split('-')[0]
                output_skill_level = output_skill.split('-')[1]

                for input_skill in input_skills:
                    input_skill_level_mapping.update({input_skill.split('-')[0] : input_skill.split('-')[1]})

                if output_skill_name in input_skill_level_mapping.keys():
                    level_choices = get_same_value_outputs(input_skill_level_mapping[output_skill_name], output_skill_level)
                else:
                    level_choices = get_single_value_outputs(output_skill_level)

                skills = []

                if level_choices:
                    skills = ['{0}-{1}'.format(output_skill_name, level_choice) for level_choice in level_choices]

                final_skillset[key] = final_skillset[key] + skills

        else:
            skills = []

            for skill in value:
                try:
                    skill_name = skill.split('-')[0]
                    skill_level = skill.split('-')[1]
                except:
                    print skill

                level_choices = get_single_value_outputs(skill_level)

                if level_choices:
                    skills = skills + ['{0}-{1}'.format(skill_name, level_choice) for level_choice in level_choices]

            final_skillset[key] = skills


    return final_skillset


if __name__ == "__main__":
    role_to_skillset_mapping = get_role_to_skillset_mapping()
    role_data = get_role_data()
    skillset_data = get_skillset_data()
    skill_data = get_skill_data()

    print "Here are the following roles: \n"

    for role in role_to_skillset_mapping.keys():
        print role

    print "\n"

    input_role = raw_input("Enter the Current role: ")
    output_role = raw_input("Enter the Destination role: ")

    final_skillset = get_role_gap(input_role, output_role, role_to_skillset_mapping)

    pprint.pprint(final_skillset)
