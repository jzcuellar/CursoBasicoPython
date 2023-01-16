"""
A child is playing with a ball on the nth floor of a tall building. 
The height of this floor above ground level, h, is known.

He drops the ball out of the window. The ball bounces (for example), 
to two-thirds of its height (a bounce of 0.66).

His mother looks out of a window 1.5 meters from the ground.

How many times will the mother see the ball pass in front of her window 
(including when it's falling and bouncing?

Three conditions must be met for a valid experiment:
- Float parameter "h" in meters must be greater than 0
- Float parameter "bounce" must be greater than 0 and less than 1
- Float parameter "window" must be less than h.

If all three conditions above are fulfilled, return a positive integer, 
otherwise return -1.

Note:
The ball can only be seen if the height of the rebounding ball is strictly
greater than the window parameter.


https://www.codewars.com/kata/5544c7a5cb454edb3c000047/python
"""

# My Solution # 1
# def bouncing_ball(h, bounce, window):
    
#     # If any of the conditions are not met return -1
#     if h <= 0 or bounce <= 0 or bounce >= 1 or window >= h:  
#         return -1
    
#     # rebotes inicia en 1 ya que si o si vera la caida
#     rebotes = 1
#     while h > window:
#         h *= bounce
#         if h > window:
#             rebotes += 2 # Se adicionan rebotes de a dos, Rebote + descenso
#     return rebotes

# Solution de ChatGPT
def bouncing_ball(h, bounce, window):
    if h <= 0 or bounce <= 0 or bounce >= 1 or window >= h:
        return -1
    
    rebotes = 1
    h *= bounce

    while h > window:
        rebotes += 2
        h *= bounce
    return rebotes

print(bouncing_ball(2, 0.5, 1))