puts 'I am in the human file'
require_relative 'mammals'
class Human < Mammal
  attr_accessor :strength, :intelligence, :stealth, :health
  def initialize
    @strength =3
    @intelligence =3
    @stealth =3
    @health =100
  end
  def attack(obj)
    if obj.class.ancestors.include?(Human)
      obj.health -= 10
      true
    else
      false
    end

  end
end

marco= Human.new
dorian= Human.new

#puts marco.attack(dorian)
#puts dorian.health
