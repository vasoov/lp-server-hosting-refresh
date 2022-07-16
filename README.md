Some organisations choose to avoid Cloud and host their APIs on bare metal servers at dedicated datacenters.
The issue that crops up in this scenario is - What hardware to procure in order to maximise ROI in terms of the number of API requests which can be served every second?
This is where Linear programming can help coupled with Python & PuLP. Linear Programming (LP, also called linear optimization) is a method to achieve the best outcome (such as maximum profit or lowest cost).

For this example, lets assume:
There is a standard server model which costs $400, uses 300W of power, takes up 2U of
a server rack, and can handle 1000 API requests/sec. There is also a cutting-edge model,
which costs $1600, uses 500W of power, but takes up only 1U, and can
handle 2000 API requests/sec. With a budget of $36,800, 44U of rack space and
12,200W of power, how many units of each model should the company purchase
in order to maximize the number of API requests it can serve every second?
