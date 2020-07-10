select Score, dense_rank() over (order by Score DESC) as 'Rank'
from Scores
order by Score DESC;

