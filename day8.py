with open('day8.txt') as f:
    lines = f.readlines()

NO_SEGMENTS_IN_8 = 7
NO_SEGMENTS_IN_7 = 3
NO_SEGMENTS_IN_4 = 4
NO_SEGMENTS_IN_1 = 2
NO_SEGMENTS_WITH_D_IN = 5

UNIQUE_SEGMENT_COUNTS = [NO_SEGMENTS_IN_8, NO_SEGMENTS_IN_7, NO_SEGMENTS_IN_4, NO_SEGMENTS_IN_1]

DIGITS = {"abcefg":'0', "cf":'1', "acdeg":'2', "acdfg":'3', "bcdf":'4', "abdfg":'5', "abdefg":'6', "acf":'7', "abcdefg":'8', "abcdfg": '9'}

def update_potential_candidates(existing_candidates, new_candidates):
    if len(existing_candidates) == 0:
        updated_candidates =  new_candidates
    else:
        updated_candidates = [i for i in existing_candidates if i in new_candidates]
    return updated_candidates


no_unique_digit_occurences = 0
sum_of_all = 0
for line in lines:
    potential_segments = {'a':set(), 'b':set(), 'c':set(), 'd':set(), 'e':set(), 'f':set(), 'g':set()}
    entry = line.rstrip().split('|')
    for digit in entry[1].split():
        if len(digit) in UNIQUE_SEGMENT_COUNTS:
            no_unique_digit_occurences += 1
    for digit in entry[0].split():
        if len(digit) == NO_SEGMENTS_IN_1:
            potential_segments['c'] = update_potential_candidates(potential_segments['c'], list(digit))
            potential_segments['f'] = update_potential_candidates(potential_segments['f'], list(digit))
        elif len(digit) == NO_SEGMENTS_IN_4:
            potential_segments['b'] = update_potential_candidates(potential_segments['b'], list(digit))
            potential_segments['c'] = update_potential_candidates(potential_segments['c'], list(digit))
            potential_segments['d'] = update_potential_candidates(potential_segments['d'], list(digit))
            potential_segments['f'] = update_potential_candidates(potential_segments['f'], list(digit))
        elif len(digit) == NO_SEGMENTS_IN_7:
            potential_segments['a'] = update_potential_candidates(potential_segments['a'], list(digit))
            potential_segments['c'] = update_potential_candidates(potential_segments['c'], list(digit))
            potential_segments['f'] = update_potential_candidates(potential_segments['f'], list(digit))
        else:
            if len(digit) == NO_SEGMENTS_WITH_D_IN:
                potential_segments['d'] = update_potential_candidates(potential_segments['d'], list(digit))
            for k in potential_segments.keys():
                potential_segments['e'].update(list(digit))
                potential_segments['g'].update(list(digit))
    
    for k in potential_segments.keys():
        if k != 'e' and k != 'g':
            updated_potential_e_segments = [i for i in potential_segments['e'] if i not in potential_segments[k]]
            updated_potential_g_segments = [i for i in potential_segments['g'] if i not in potential_segments[k]]
            potential_segments['e'] =  updated_potential_e_segments
            potential_segments['g'] =  updated_potential_g_segments
    for k in potential_segments.keys():
        if k != 'c' and k!= 'f':
            updated_potential_segments = [i for i in potential_segments[k] if i not in potential_segments['c']]
            potential_segments[k] =  updated_potential_segments
    potential_segments_copy = potential_segments.copy()
    for key_taken,val_taken in potential_segments_copy.items():
        if len(val_taken) == 1:
            for k in potential_segments.keys():
                if k != key_taken:
                    updated_potential_segments = [i for i in potential_segments[k] if i not in val_taken]
                    potential_segments[k] =  updated_potential_segments

    for digit in entry[0].split():
        if len(digit) == NO_SEGMENTS_WITH_D_IN:
            if len(potential_segments['b']) == 1:
                if potential_segments['b'][0] in digit:
                    updated_potential_e_segments = [i for i in potential_segments['e'] if i not in digit]
                    potential_segments['e'] = updated_potential_e_segments
                    updated_potential_c_segments = [i for i in potential_segments['c'] if i not in digit]
                    potential_segments['c'] = updated_potential_c_segments
            if len(potential_segments['f']) == 1:
                if potential_segments['f'][0] in digit:
                    updated_potential_e_segments = [i for i in potential_segments['e'] if i not in digit]
                    potential_segments['e'] = updated_potential_e_segments
            if len(potential_segments['e']) == 1:
                if potential_segments['e'][0] in digit:
                    updated_potential_f_segments = [i for i in potential_segments['f'] if i not in digit]
                    potential_segments['f'] = updated_potential_f_segments
                    updated_potential_b_segments = [i for i in potential_segments['b'] if i not in digit]
                    potential_segments['b'] = updated_potential_b_segments
            if len(potential_segments['c']) == 1:
                if potential_segments['c'][0] in digit:
                    updated_potential_b_segments = [i for i in potential_segments['b'] if i not in digit]
                    potential_segments['b'] = updated_potential_b_segments
    potential_segments_copy = potential_segments.copy()
    for key_taken,val_taken in potential_segments_copy.items():
        if len(val_taken) == 1:
            for k in potential_segments.keys():
                if k != key_taken:
                    updated_potential_segments = [i for i in potential_segments[k] if i not in val_taken]
                    potential_segments[k] =  updated_potential_segments
    #print(potential_segments)

    #Decode
    decoder_lookup = {v[0]:a for a,v in potential_segments.items()}
    val = ""
    for digit in entry[1].split():
        decoded_digit =""
        for c in digit:
            decoded_digit += decoder_lookup[c]
        val += DIGITS["".join(sorted(decoded_digit))]
    sum_of_all += int(val)



print(f"part1: {no_unique_digit_occurences}")
print(f"part2: {sum_of_all}")
