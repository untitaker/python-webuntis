import datetime
from typing import Any, Union

import objects


class JSONRPCSession:
    config: Any = ...

    def __init__(self, **kwargs) -> None: ...

    def __enter__(self): ...

    def __exit__(self, exc_type, exc_value, traceback): ...

    def logout(self, suppress_errors: bool = ...) -> None: ...

    def login(self) -> Session: ...


class ResultWrapperMixin:
    def departments(self) -> objects.DepartmentList: ...

    def holidays(self) -> objects.HolidayList: ...

    def klassen(self, schoolyear: Union[objects.SchoolyearObject, int] = ...) -> objects.KlassenList: ...

    def timetable(self,
                  start: Union[datetime.datetime, datetime.date, int],
                  end: Union[datetime.datetime, datetime.date, int], **type_and_id) -> objects.PeriodList: ...

    def rooms(self) -> objects.RoomList: ...

    def schoolyears(self) -> objects.SchoolyearList: ...

    def subjects(self) -> objects.SubjectList: ...

    def teachers(self) -> objects.TeacherList: ...

    def statusdata(self) -> objects.StatusData: ...

    def last_import_time(self) -> objects.TimeStampObject: ...

    def substitutions(self, start: Union[datetime.datetime, datetime.date, int],
                      end: Union[datetime.datetime, datetime.date, int],
                      department_id: int = ...) -> objects.SubstitutionList: ...

    def timegrid_units(self) -> objects.TimegridObject: ...

    def students(self) -> objects.StudentsList: ...

    def exam_types(self) -> objects.ExamTypeList: ...

    def exams(self, start: Union[datetime.datetime, datetime.date, int],
              end: Union[datetime.datetime, datetime.date, int], exam_type_id: int = ...) -> objects.ExamsList: ...

    def timetable_with_absences(self, start: Union[datetime.datetime, datetime.date, int],
                                end: Union[datetime.datetime, datetime.date, int]) -> objects.AbsencesList: ...

    def class_reg_events(self, start: Union[datetime.datetime, datetime.date, int],
                         end: Union[datetime.datetime, datetime.date, int]) -> objects.ClassRegEventList: ...

    def class_reg_event_for_id(self, start: Union[datetime.datetime, datetime.date, int],
                               end: Union[datetime.datetime, datetime.date, int],
                               **type_and_id) -> objects.ClassRegEventList: ...

    def class_reg_categories(self) -> objects.ClassRegCategoryList: ...

    def class_reg_category_groups(self) -> objects.ClassRegCategoryGroupList: ...

    def get_student(self, surname: str, fore_name: str, dob: int = ...) -> objects.StudentObject: ...

    def get_teacher(self, surname: str, fore_name: str, dob: int = ...) -> objects.TeacherObject: ...


class Session(JSONRPCSession, ResultWrapperMixin):
    cache: Any = ...
    config: Any = ...

    def __init__(self, **config) -> None: ...
