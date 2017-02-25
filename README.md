# spacegame

Meanings:
() - create a instance in that class
no() - put some instance already create in that class

Logic:
Universe()  |Galaxy()   |PlanetarySystem()  |Planet()
            |Player()	|Planet     |Resource()
            |           |           |Mine() |Resource
            |           |		    |Storage()  |Resource
		    |		    |		    |Factory()  |Building
		    |		    |		    |Hangar()   |SpaceShip()    |Weapon
		    |		    |		    |		    |			    |Shield
		    |		    |		    |		    |			    |Engine
		    |		    |		    |		    |Defense()		|Weapon
		    |		    |		    |		    |			    |Shield
		    |		    |		    |		    |Weapon()
		    |		    |		    |		    |Shield()
		    |		    |		    |		    |Engine()
            |           |           |           |Fleet()
		    |		    |		    |           |Flight()
		    |		    |		    |ResearchLab()  |Research()
		    |		    |		    |Defense
		    |		    |		    |Battle()   |Forces()
            |           |           |Fleet
		    |		    |Research
		    |
            |Battle

Presentation()  |Resources()
			    |Menu() |Overview() |Player
				|		|           |Planet
			    |		|Buildings()    |Header()
			    |		|			    |Fill()
			    |		|Merchant()
			    |		|Researches()
			    |		|Hangar()
			    |		|Defenses()
			    |		|Fleet()
			    |		|Universe()
			    |		|Alliance()
