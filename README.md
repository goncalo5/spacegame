# spacegame

Meanings:
() - create a instance in that class
no() - put some instance already create in that class

Logic:
Universe()  |Galaxy()   |PlanetarySystem()	|Planet()
		        |Player()		|Planet	  |Resource()
		        |           |		      |Mine()	   |Resource
		        |		        |		      |Storage() |Resource
		        |		        |		      |Factory() |Building
		        |		        |		      |Hangar()	 |SpaceShip()	|Weapon
		        |		        |		      |		       |			      |Shield
		        |		        |		      |		       |			      |Engine
		        |		        |		      |		       |Defense()		|Weapon
		        |		        |		      |		       |			      |Shield
		        |		        |		      |		       |Weapon()
		        |		        |		      |		       |Shield()
		        |		        |		      |		       |Engine()
		        |		        |		      |ResearchLab()	|Research()
		        |		        |		      |Fleet()
		        |		        |		      |Defense
		        |		        |		      |Battle()	|Fleet
		        |		        |Research
		        |           
            |Battle

Presentation() |Resources()
			         |Menu()	 |Overview()	|Player
					     |			   |            |Planet
			         |		     |Buildings()	|Header()
			         |		     |			      |Fill()
			         |		     |Merchant()
			         |		     |Researches()
			         |		     |Hangar()
			         |		     |Defenses()
			         |		     |Fleet()
			         |		     |Universe()
			         |		     |Alliance()
