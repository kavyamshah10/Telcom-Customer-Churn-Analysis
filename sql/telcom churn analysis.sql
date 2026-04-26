select * from telcom


--1) total customer
select count(*) as total_customers
from telcom;

--2) total churned customer
SELECT COUNT(*) AS churned_customer
FROM telcom
WHERE "Churn" = 'Yes';

--3)churn rate%
SELECT
    ROUND(
        COUNT(CASE WHEN telcom."Churn" = 'Yes' THEN 1 END) * 100.0 / COUNT(*), 2
    ) AS churn_rate
FROM telcom;

--4)average monthly charges by churn
SELECT 
    telcom."Churn",
    AVG(telcom."MonthlyCharges") AS avg_monthly_charges
FROM telcom
GROUP BY telcom."Churn";

--5)contract type vs churn
select telcom."Contract",
count(*) as total_customer,
sum(CASE WHEN telcom."Churn" = 'Yes' THEN 1 ELSE 0 END) as churned
from telcom
group by telcom."Contract"
order by churned desc;

--6)tenure group analysis
select 
case when telcom."tenure"<12 then '0-1 Year'
     when telcom."tenure" between 12 and 24 then '1-2 Years'
	 ELSE '2+ Years'
END as tenure_group,
count(*)as total,
sum(CASE WHEN telcom."Churn" = 'Yes' THEN 1 ELSE 0 END) as churned
from telcom
group by tenure_group

--7)revenue loss due to churn
select
sum(telcom."MonthlyCharges") AS revenue_loss
FROM telcom
where telcom."Churn"='Yes';

--8)payment method impact on churn
select telcom."PaymentMethod",
count(*)as total,
sum(CASE WHEN telcom."Churn" = 'Yes' THEN 1 ELSE 0 END) as churned
from telcom
group by telcom."PaymentMethod"
order by churned desc;

--9)top feature influencing churn
select telcom."InternetService",
count(*)as total,
sum(CASE WHEN telcom."Churn" = 'Yes' THEN 1 ELSE 0 END) as churned
from telcom
group by telcom."InternetService"
order by churned desc;

--10)high risk customer
select telcom."Churn",count(*)
from telcom
where telcom."Contract"='Month-to-month'
and telcom."MonthlyCharges">70
and telcom."tenure"<12
group by telcom."Churn";






	 