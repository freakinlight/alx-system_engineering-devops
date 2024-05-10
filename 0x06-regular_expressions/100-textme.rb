#!/usr/bin/env ruby

# Function to extract sender, receiver, and flags from log entry
def extract_info(log_entry)
  sender = log_entry.match(/\[from:(.+?)\]/)[1]
  receiver = log_entry.match(/\[to:(.+?)\]/)[1]
  flags = log_entry.match(/\[flags:(.+?)\]/)[1]
  "#{sender},#{receiver},#{flags}"
end

# Main method
def main
  # Read log entries from stdin or file
  if ARGV.empty?
    puts "Usage: #{$PROGRAM_NAME} logfile"
    exit 1
  end

  # Extract information for each log entry
  File.open(ARGV[0]).each_line do |line|
    if line.include?('Sent SMS') || line.include?('Receive SMS')
      puts extract_info(line)
    end
  end
end

# Run main method if script is executed directly
if __FILE__ == $PROGRAM_NAME
  main
end

