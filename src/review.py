import json

class Review:
  def __init__(self, review_id, user_id, business_id, stars, useful, funny, cool, text, date):
    self.review_id = review_id
    self.user_id = user_id
    self.business_id = business_id
    self.stars = stars
    self.useful = useful
    self.funny = funny
    self.cool = cool
    self.text = text
    self.date = date