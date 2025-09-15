#49
def solution(new_id):
    # 아이디의 길이는 3자 이상 15자 이하
    # 알파벳 소문자, 숫자, 빼기(-), 밑줄(_), 마침표(.) 문자만 사용할 수 있습니다
    # 마침표(.)는 처음과 끝에 사용할 수 없으며 또한 연속으로 사용할 수 없습니다.
    # 모든 대문자를 대응되는 소문자로 치환
    new_id = new_id.lower()
    # print(1, new_id)
    # 알파벳 소문자, 숫자, 빼기(-), 밑줄(_), 마침표(.)를 제외한 모든 문자를 제거
    for k in new_id:
        if k in "~!@#$%^&*()=+[{]}:?,<>/": new_id = new_id.replace(k, '')
    print(2, new_id, len(new_id))
#     # 마침표(.)가 2번 이상 연속된 부분을 하나의 마침표(.)로 치환합니다.
#     # 흠 뭔가 더 좋은코드로 할수없ㅇ르까?
    while '..' in new_id: 
        new_id = new_id.replace('..', '.')
        
    # 마침표(.)가 처음이나 끝에 위치한다면 제거
    while new_id.startswith('.'): 
        new_id = new_id[1:]
    # print(3, new_id)
    while new_id.endswith('.'): 
        new_id = new_id[:-1]
    # print(4, new_id)
    # 빈 문자열이라면, new_id에 "a"를 대입합니다.
    if len(new_id) == 0: new_id += 'a' # not new_id도 되는지 확인
    # print(5, new_id)
    # new_id의 길이가 16자 이상이면, new_id의 첫 15개의 문자를 제외한 나머지 문자들을 모두 제거합니다.
    if len(new_id) >= 16: 
        new_id = new_id[:15]
        # 만약 제거 후 마침표(.)가 new_id의 끝에 위치한다면 끝에 위치한 마침표(.) 문자를 제거합니다.
        if new_id.endswith('.'): new_id = new_id[:-1]
    # print(6, new_id)
    # new_id의 길이가 2자 이하라면, new_id의 마지막 문자를 new_id의 길이가 3이 될 때까지 반복해서 끝에 붙입니다.
    while len(new_id) <= 2: 
        new_id += new_id[-1]
    print(7, new_id)
    
    
                             
    return new_id