#!/usr/bin/env ruby
# a regular expression that will match the given cases

puts ARGV[0].scan(/hbt{2,5}n/).join
