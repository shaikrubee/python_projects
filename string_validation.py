UPPER_CASE_LETTERS="ABCDEFGHIGKLMNOPQRSTUVWXYZ"
def is_upper_case_letter(character):
    return character in UPPER_CASE_LETTERS


def is_underscore(character):
    return character=="_"

def all_satisfied(results):
    final_result=True   
    for result in results:
        final_result=final_result and result
        
    return final_result

def get_no_of_words(S):
    return len(S.split('_'))  

def is_valid_string(S):
    results=[]
    for character in S:
        result=is_upper_case_letter(character) or is_underscore(character)
        results.append(result)
    return all_satisfied(results)

def main():
    S=input()
    is_valid=is_valid_string(S) 
    if is_valid:
        result="True "+str(get_no_of_words(S))
    else:
        result="False"
    print(result)

main()