class Student:
    def __init__(self,name,grade,score):
        self.name=name
        self.grade=grade
        self.score=score
    
st1= Student()

print(f'{st1.grade}학년 {st1.name}의 성적은 {st1.score}입니다.')

st2=Student('홍길동',2,'B')
print(f'{st2.grade}학년 {st2.name}의 성적은 {st2.score}입니다.')