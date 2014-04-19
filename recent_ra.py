#!/usr/bin/python

# Updates rarecs_log.txt if there is new "RA Recommends" data
# from Resident Advisor.  

# Requires ra-recommends module at
# https://github.com/oldhill/ra-recommends

import ra_recommends.rarecommends as rarecommends

def main():

  # Get historical data from disc
  history_file = open('rarecs_log.txt', 'r')
  full_history_log = history_file.read()
  latest_historical_set = full_history_log.split('\n')[0] #first line
  history_file.close()

  # Grab latest data from residentadvisor.net/reviews.aspx?format=recommend
  current_artist = rarecommends.recommendedArtist()
  current_work = rarecommends.recommendedWork()
  current_set = current_artist+' -- '+current_work
  
  # Debug 
  print 'latest:  '+latest_historical_set
  print 'current: '+current_set

  # If there's a new set, write new history file
  if current_set != latest_historical_set:

    new_log = current_set+'\n'+full_history_log
    updated_history_file = open('rarecs_log.txt', 'w')
    updated_history_file.write(new_log)
    updated_history_file.close()
    print 'file updated!'

  else:

    print 'no updates'

if __name__ == '__main__':
  main()
