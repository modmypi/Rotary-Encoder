require 'rpi_gpio'

RPi::GPIO.set_numbering :bcm

CLOCK = 17
DATA = 18

RPi::GPIO.setup(CLOCK, as: :input)
RPi::GPIO.setup(DATA, as: :input)

def dtState
  RPi::GPIO.high?(DATA) ? 1 : 0
end

def clock_state
  RPi::GPIO.high?(CLOCK) ? 1 : 0
end

counter = 0
clock_last_state = clock_state

loop do
  if clock_state != clock_last_state
    if dtState != clock_state
      counter += 1
    else
      counter -= 1
    end

    puts counter
  end

  clock_last_state = clock_state
  sleep 0.01
end

at_exit do
  RPi::GPIO.clean_up
end
