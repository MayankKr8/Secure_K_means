# Secure_K_means
This repository covers my work on devising and  implemnting a secure approach to K-means clustering, as part of my B.Tech Project(BTP). The project was guided by and submitted to [Dr K.K. Shukla](https://www.iitbhu.ac.in/dept/cse/people/kkshuklacse)

Outsourcing data for third party analysis raises data privacy preservation concerns, hence questioning the viability of the system. Data confidentiality is ensured through cryptography techniques. Any form of sophisticated analysis is precluded upon using techniques like Homomorphic encryption, that allow limited amount of data manipulation. 

We couple encrypted data with additional information for this to be achieved to facilitate third party analysis. The work is based on a mechanism for Homomorphically secure k-means clustering and the concept of an Updatable Distance Matrix (UDM). Both data privacy and correctness are preserved when the proposed mechanism thus allows the application of clustering algorithms to encrypted data.

How to run?
--------------------
* The intuitive naming suggests that there are two modules to be run, one at the third party and another at the data owner. 
* Place the traiing set with the data owner and pickled files at a secure shared location accessible to both data owner and third *party only.(You might have to change the file commands in the module, based on the locations.) 
* Run the modules,simultaneously, they communicate and provide you results. 
* Once clustering is done, it is stored in pickled file for future uses.
