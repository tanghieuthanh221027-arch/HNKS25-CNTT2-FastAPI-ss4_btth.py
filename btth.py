from fastapi import FastAPI , HTTPException

app = FastAPI()

courses = [
    {
        "id": 1,
        "name": "Python Basic",
        "category": "backend",
        "price": 3000000,
        "mode": "online"
    },
    {
        "id": 2,
        "name": "Java Web",
        "category": "backend",
        "price": 5000000,
        "mode": "offline"
    },
    {
        "id": 3,
        "name": "Web Frontend",
        "category": "frontend",
        "price": 4000000,
        "mode": "online"
    }
]

@app.get("/courses")
def get_courses():
    return courses

@app.get("/courses/search")
def filter_course(mode: str = None, category: str = None):
    result = courses

    if mode:
        found_by_mode = []

        for course in result:
            if mode.lower() == course["mode"].lower():
                found_by_mode.append(course)

        if len(found_by_mode) == 0:
            raise HTTPException(
                status_code=400,
                detail="Hình thức học không hợp lệ"
            )

        result = found_by_mode

    if category:
        found_by_category = []

        for course in result:
            if category.lower() == course["category"].lower():
                found_by_category.append(course)

        if len(found_by_category) == 0:
            raise HTTPException(
                status_code=400,
                detail="Nhóm khóa học không hợp lệ"
            )

        result = found_by_category

    return {
        "data": result
    }

@app.get("/courses/{course_id}")
def get_course_detail(course_id : int):
    for course in courses : 
        if course['id'] == course_id:
            return {
                "message" : f"Chi tiết khóa học có mã {course_id}",
                "data" : course
            }
    
    raise HTTPException(
        status_code=404,
        detail= f"Không có khóa học có mã {course_id}"
    )