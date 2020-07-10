# Write your MySQL query statement below
SELECT  ifnull(ROUND(COUNT(DISTINCT session_id)/COUNT(DISTINCT user_id),2),0.0) AS average_sessions_per_user
    FROM Activity
    WHERE activity_date >= DATE("2019-06-28")
    AND activity_date <= DATE("2019-07-27")

##
   where DATEDIFF('2019-07-27', activity_date) < 30;
