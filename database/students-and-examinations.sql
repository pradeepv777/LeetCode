select
    ss.student_id,
    ss.student_name,
    ss.subject_name,
    count(e.subject_name) as attended_exams
from
(
    select
        s.student_id,
        s.student_name,
        sub.subject_name
    from students s, subjects sub
) ss
left join examinations e
on ss.student_id = e.student_id
and ss.subject_name = e.subject_name
group by
    ss.student_id,
    ss.student_name,
    ss.subject_name
order by
    ss.student_id,
    ss.subject_name;