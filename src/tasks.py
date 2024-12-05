from crewai import Task
from textwrap import dedent
from datetime import date


class TripTasks():
  def gather_task(self, agent:str, city:str, interests:str):
    return Task(
        description=dedent(f"""
        As a local expert on this city you must compile an 
        in-depth guide for someone traveling there and wanting 
        to have THE BEST trip ever!
        Gather information about  key attractions, local customs,
        special events, and daily activity recommendations.
        Find the best spots to go to, the kind of place only a
        local would know.
        This guide should provide a thorough overview of what 
        the city has to offer, including hidden gems, cultural
        hotspots, must-visit landmarks, weather forcast, and
        high level costs.
        
        The final answer must be a comprehensive city guide, 
        rich in cultural insights and practical tips, 
        tailored to enhance the travel experience.
        {self.__tip_section()}

        Traveler Interests: {interests}
        city: {city}
      """),
        expected_output="""A comprehensive city guide in markdown 
        format that includes attractions, local customs, events, and recommendations.""",
        agent=agent
    )

  def plan_task(self, agent:str, interests:str, date_range:str, context:list):
    return Task(
        description=dedent(f"""
        Expand this guide into a a full {date_range} day travel 
        itinerary with detailed per-day plans, including 
        weather forecasts, places to eat, packing suggestions, 
        and a budget breakdown.
        
        You MUST suggest actual places to visit, actual hotels 
        to stay and actual restaurante to go to.
        
        This itinerary should cover all aspects of the trip, 
        from arrival to departure, integrating the city guide
        information with practical travel logistics.
        
        Your final answer MUST be a complete expanded travel plan,
        formatted as markdown, encompassing a daily schedule,
        anticipated weather conditions, recommended clothing and
        items to pack, and a detailed budget, ensuring THE BEST
        TRIP EVER, Be specific and give it a reason why you picked
        # up each place, what make them special! {self.__tip_section()}

        Traveler Interests: {interests}
      """),
        expected_output="""A detailed day-by-day travel itinerary in 
        markdown format, including weather forecasts, accommodations, 
        restaurants, and budget breakdown.""",
        agent=agent,
        context=context
    )

  def __tip_section(self):
    return "If you do your BEST WORK, I'll tip you $100!"