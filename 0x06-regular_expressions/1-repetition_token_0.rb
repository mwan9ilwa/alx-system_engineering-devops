#!/usr/bin/env ruby
#Matches case of repetition of given letters
puts ARGV[0].scan(/hbt{2,5}n$/).join
