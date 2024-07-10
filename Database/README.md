# water Quality Dataset

The dataset contains the following columns:
- ph
- Hardness
- Solids
- Chloramines
- Sulfate
- Conductivity
- Organic_carbon
- Trihalomethanes
- Turbidity
- Potability


### The schema will contain two tables:
- `WaterQuality`: This table will contain all the columns except `Potability`.
- `WaterPotability`: This table will contain the `Potability` information along with a foreign key linking to the `WaterQuality` table.


Here’s a possible design for the schema:
### Table: WaterQuality
- id (Primary Key)
- ph
- Hardness
- Solids
- Chloramines
- Sulfate
- Conductivity
- Organic_carbon
- Trihalomethanes
- Turbidity

### Table: WaterPotability
- id (Primary Key)
- water_quality_id (Foreign Key referencing WaterQuality(id))
- Potability


### Database
The database of choice is going to be postgresQl 
