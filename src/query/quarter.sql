-- Number of employees hired for each job and department in 2021 divided by quarter
WITH quarter_distrib AS 
(
    SELECT  empl.id, 
            empl.datetime,
            dept.department, 
            job.job, 
            NTILE(4) OVER(PARTITION BY dept.department, job.job ORDER BY empl.datetime) AS quarter_num 
    FROM hired_employees AS empl 
    INNER JOIN departments AS dept 
        ON empl.department_id = dept.id 
    INNER JOIN jobs AS job 
        ON empl.job_id = job.id 
    WHERE strftime('%Y', empl.datetime) = '2021' 
), Q1 AS (
    SELECT  department, 
            job, 
            COUNT(quarter_num) AS Q1 
    FROM quarter_distrib 
    WHERE   quarter_num = 1 
    GROUP BY department, job 
), Q2 AS (
    SELECT  department, 
            job, 
            COUNT(quarter_num) AS Q2 
    FROM quarter_distrib 
    WHERE   quarter_num = 2 
    GROUP BY department, job 
), Q3 AS (
    SELECT  department, 
            job, 
            COUNT(quarter_num) AS Q3 
    FROM quarter_distrib 
    WHERE   quarter_num = 3 
    GROUP BY department, job 
), Q4 AS (
    SELECT  department, 
            job, 
            COUNT(quarter_num) AS Q4 
    FROM quarter_distrib 
    WHERE   quarter_num = 4 
    GROUP BY department, job 
) 
SELECT  
    Q1.department, 
    Q1.job, 
    Q1.Q1, 
    Q2.Q2, 
    Q3.Q3, 
    Q4.Q4 
FROM Q1 
    INNER JOIN Q2 ON Q1.department = Q2.department AND Q1.job = Q2.job
    INNER JOIN Q3 ON Q1.department = Q3.department AND Q1.job = Q3.job
    INNER JOIN Q4 ON Q1.department = Q4.department AND Q1.job = Q4.job
ORDER BY Q1.department, Q1.job