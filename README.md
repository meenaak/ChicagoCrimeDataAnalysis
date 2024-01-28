
# ChicagoCrimeDataAnalysis
Dataset- https://data.cityofchicago.org/Public-Safety/Crimes-2001-to-Present/ijzp-q8t2

# Step 1: Load the Data
We can start by downloading the Chicago crime dataset on kaggle.com. Once the dataset is downloaded, we place the CSV files in our working folder. The dataset contains all the incidents of crime that occured in Chicago from 2010 to present. We will use only the CSV's from 2020 to 2022. Once we have successfully read the files, we exclude the columns that we will not use for our analysis (for example "Ward", "District"). The columns that remain in our dataset are:

ID: Unique identifier of the record
Date: Timestamp of the crime incident
Block: The block address of the crime incident
Primary Type: Type of crime incident. This variable will later be used as target variable
Location Description: The type of location that the crime took place
Arrest: Indicates whether an arrest was made
Community Area: Indicates the number of the community area where the incident occurred
Name: Indicates the name of the community area where the incident occurred (only in chicagopop.csv)
Population: Population of the community area where the incident occurred (only in chicagopop.csv)
Area: Indicates the area where the incident occurred (only in chicagopop.csv)
Latitude: Indicates the latitude of the location where the incident occurred
Longitude: Indicates the longitude of the location where the incident occurred
Year: We extract this from the date column, year of the occurred incident
Month: We extract this from the date column, month of the occurred incident
Hour: We extract this from the date column, hour of the occurred incident
Once we load the data into dataframes and concat them into one dropping na values, we use the head() command to ensure that we can see the data.

![image](https://github.com/meenaak/ChicagoCrimeDataAnalysis/assets/37869066/da8b0333-fb31-4929-8bbb-332ee1677486)




Next, we have to merge df, with the pop dataframe to get the remaining columns. Full code is available on the uploaded files.

Step 2: Explore the data
At the beginning of a project, it is usual to not quite understand the data very well. For this reason, the following examples will help us understand them better.

2.1 Primary Type frequency

The plot below shows the frequency of the Primary type labels that occur in our data

![image](https://github.com/meenaak/ChicagoCrimeDataAnalysis/assets/37869066/82a68ba6-7ae9-474c-8744-10ce31c0e447)


Theft and battery are the most frequent crimes that occur in Chicago. We can easily observe that our data is highly imbalanced. This will affect the accuracy of the model that we will use later, so we have to consider this when we will measure its performance.

2.2 Crime map of Chicago

Next, we can use the Plotly library of Python to create a Chicago crime map. For this purpose, we will use only the 4% of our data for this plot, due to the plugin's capacity constraints for processing data at the same time. The end result is an interactive map of Chicago that demonstrates how each crime type is distributed across the city.

Below we can see the distribution of the most often Primary type, which is Theft (as shown from the previous plot).

![image](https://github.com/meenaak/ChicagoCrimeDataAnalysis/assets/37869066/154b3d70-432f-4d4d-80d4-edff1978289d)


We observe that theft is more intense in the east of Chicago, and next in the northeast. We can use this crime map to see the distribution of other crimes also. If we hover over a dot, we can see the details we have of the specific crime.

2.3 At what time a crime occured

With the following plot we select the most common types of crime, and we see how they behave throughout the day.

![image](https://github.com/meenaak/ChicagoCrimeDataAnalysis/assets/37869066/9b98362c-61c9-4079-8db5-97433d6a55d1)


Our findings suggest that criminals are more active during the early afternoon and midnight. The peak of the most common crime occurs most often at 19:00. Also, there are crimes such as "NARCOTICS" that occur rarely in the night, but most of the times in the day.

If we want, we can be more specific and add more parameters (for example when the location is "Residence" or "Apartment")

2.4 In which area the most crime incidents are recorded

Using a bar chart of Plotly, we can find out which area records the most crime incidents in Chicago.

![image](https://github.com/meenaak/ChicagoCrimeDataAnalysis/assets/37869066/511a18ac-4fc2-4c3a-a1d7-edf191f83689)


West Side is by far the busiest area, and on the contrary, the least crime incidents are recorded in the north.

2.5 Crime heatmap of Chicago

With the Python library folium, we can create a heatmap of Chicago to visualize the density of criminal activity in the city.

![image](https://github.com/meenaak/ChicagoCrimeDataAnalysis/assets/37869066/6b9efa47-cb2b-4012-9879-6c37d24a528e)


The most heavily affected part of Chicago is in the Central region, and upon zooming in the map we can find the North State Street that stands out as a hotspot. This street is one of the most popular shopping destinations of the city, and is also the block with the most crime incidents recorded (particularly theft).

2.6 Location analysis on a specific day

Proceeding with the analysis, we can become more specific and visualize the crimes that occurred a specific day, on a specific location of Chicago. If we group our data by date, we will find out that the date with the most crime incidents occur on 31st of May 2020 (George Floyd protests). We can choose one of the 77 community areas, we will pick for this example Near West Side.

![image](https://github.com/meenaak/ChicagoCrimeDataAnalysis/assets/37869066/f8eba10e-ebca-4ea5-9ccf-3c3023a1da44)


The first step is to visualize all the crimes that occurred with a heatmap on the location. Next, using the latitude and longitude of these crimes, we find the centroid of these incidents and mark it with a black circle. In case we have one ambulance or patrol car available, it would be most efficient to place it in the spot of this circle, for quickest average response time. Therefore, it would be beneficial to station emergency services between Eisenhover Expressway and South Ashland Avenue, in the event of similar situations in the future.

Additional visualizations, deeper analysis and complete code are available on the dashboards files. While there is still room for further exploration, we have a solid understanding of the data, and we can continue with clustering.

Step 3: Clustering
Clustering is a technique that groups similar data points together without using pre-labeled information. This process organizes data into various sets based on how closely they resemble each other. We will apply this method to discover the similarities between different regions in Chicago by utilizing the types of crimes recorded in each area.

3.1 Finding the optimal number of clusters

First, we have to find the K number, that will make our number of clusters optimal. To achieve this, we will use The Elbow method. The Elbow Method is a widely used approach to determine the ideal number of clusters in a given dataset. This method utilizes the Within Cluster Summed Squares (WCSS) parameter, which is calculated based on the location of the centroids of each group. The WCSS parameter decreases as the number of clusters increases. As more clusters are added, the difference in decrease of WCSS becomes less significant. The optimal number of clusters is reached when the decrease in WCSS is not significant.

![image](https://github.com/meenaak/ChicagoCrimeDataAnalysis/assets/37869066/784861d3-711b-4d3b-8e4a-41ede7bddded)


Based on the image above, there is a significant difference when the number of clusters is 3. Once this number is reached, the distinction between clusters becomes less significant. In this example, the optimal number of clusters is 3.

3.2 Division of Chicago regions

We can observe the geographical location of each cluster with the help of a map created with the Plotly library, in order to identify each region by its corresponding cluster colour assigned by the K-Means algorithm.

![image](https://github.com/meenaak/ChicagoCrimeDataAnalysis/assets/37869066/0b4058a4-8fad-4341-b741-a38410f423f7)


We can notice that there is a geographical relationship in the way our clusters are grouped, thus we can make observations about the division of them and the regions they contain.

Cluster 1

Regions: Far North Side, Far Southeast Side, South Side, Southwest Side

The areas that participate in this cluster are located mainly in the southern part of Chicago. These areas have the highest crime rates, and all of them are characterized by high incidents of battery

Cluster 2

Regions: West Side

On this cluster participates only the West Side of Chicago. However, it is the cluster with the highest number of crimes. The difference compared to the rest of the regions is so significant to the point that the region is classified in a cluster by itself. The most prevalent crimes in West Side are battery and theft

Cluster 3

Regions: Central, Far Southwest Side, Far North Side, North Side, Northwest Side

The last cluster includes the areas that make up the northern part of Chicago, as well as its center. These areas are grouped into a cluster due to their comparatively low number of recorded crimes than the rest of the city, with theft being the most frequent type of crime recorded.

Step 4: Prediction model
Our target is to develop a model that can make predictions of the type of a crime with high accuracy, giving to the model as input, features like date and the area. To achieve this, we use Random Forest Classifier. Random Forest is a machine learning technique, used to solve classification and regression problems. It combines multiple decision trees and uses ensemble learning, which combines multiple classifiers to tackle complex problems. The algorithm can only handle integer and boolean values, but no categorical data. Therefore, we need to prepare our data before utilizing Random Forest.

From our dataset, we will use in our model the features:

Date & Time: The date and time feature plays a crucial role in our model as it helps to understand certain patterns of crimes. For instance, the nightlife district experiences an increase in certain types of crimes during Saturday nights due to the presence of more people.

Area: In order to add area feature, we have to use dummy variables, since we have already mentioned that our model will be able to handle only integer and boolean values.

Latitude & Longitude: For the latitude and longitude features, we firstly remove the outliers of our dataset. Then, we convert them into polar coordinates. This allows our model to better understand the location.

Taking account of these features, the primary input to our crime type prediction model is the information of the time and location where a crime takes place.

The next step is to divide our data into two separate sets, one for training and one for testing. We will use 80% of the data for training and the remaining 20% for testing. Once this is done, we can use the training dataset to train our Random Forest model.

![image](https://github.com/meenaak/ChicagoCrimeDataAnalysis/assets/37869066/2d28c9d0-7ad0-4bc6-8904-df338c5c6fc4)


Our model achieves 28% accuracy. At first glance, this might not seem very impressive, but considering that we have 32 types of crime and only 620.000 records in our dataset, the number is respectable. Lastly, let's observe some predictions made by our model and compare them to the actual crime types.

![image](https://github.com/meenaak/ChicagoCrimeDataAnalysis/assets/37869066/539d1f4f-211f-46e2-b327-4d522b85b2d6)


Our model mostly predicts the labels of crimes of 1 and 4. This is also confirmed by the confusion matrix below.

![image](https://github.com/meenaak/ChicagoCrimeDataAnalysis/assets/37869066/07dc9cc6-7b1c-413b-9b61-1dd8c05be676)


The confusion matrix shows that our model frequently predicts crime categories 1 and 4, neglecting the rest crime types. This is due to the uneven distribution of crime types in the training data.

# Conclusion
This crime analysis presents multiple ways to visualize our data, so we can have a better understanding of them. We depicted our data in an interactive map of Chicago, using Plotly library, and we also used heatmaps in order to highlight hotspots. Furthermore, we divided the city of Chicago into 3 clusters based on the location and frequent crime types in each region. Finally, we trained a Random Forest Classifier model with 28% accuracy, a satisfying result, considering our dataset is highly imbalanced and contains 32 possible crime types.
