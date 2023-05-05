select title.worker_title best_paid_title from worker join title
on title.worker_ref_id=worker.worker_id
where worker.salary= (select max(salary) from worker);