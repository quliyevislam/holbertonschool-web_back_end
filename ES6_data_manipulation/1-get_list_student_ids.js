const getListStudentIds = (students = []) => {
    const id = [];
    
    if (!Array.isArray(students)) {
        return id;
    }
    for (let student of students) {
        id.push(student.id);
    }
    return id;
}
export default getListStudentIds;