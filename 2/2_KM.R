# Written by : Atul Patare (github.com/AP-Atul)
########################################################
NOP = 20 # number of points
NOC = 2 # number of clusters is always 2
ITR = 100 # number of iterations
THRESH = 0.1 # difference threshold

########################################################
# function for KMeans clustering, loop through the dset
KMeansClustering <- function(data, n){
  x = data[ , 1]
  y = data[ , 2]
  d = matrix(data = NA, ncol = 0, nrow = 0)

  # select partition of the dataset
  for (i in 1 : n){
    d = c(d, c(x[i], y[i]))
  }

  # copying the dataset
  init <- matrix(d, ncol=2, byrow=TRUE)
  oldMeans <- init

  # create a cluster for init dset
  cl = CreateCluster(data, oldMeans)

  # update the mean dset with new means
  means = UpdateMean(data, cl, n)

  # cal distances
  threshold = Delta(oldMeans, means)

  print(threshold)
  # loop till the distance is greater than the min
  while(threshold > THRESH){
    cl = CreateCluster(data, means)
    oldMeans = means
    means = UpdateMean(data, cl ,n)
    thr = Delta(oldMeans, means)
  }

  for (e in 1 : n){
    group = which(cl == e)

    plot(data[group, ], axes = F, col = e, xlim = c(1, n), ylim = c(1, n), pch = 20, xlab = "Species", ylab = "Sepals")
    par(new = T)
  }

  plot(data[means, ], axes = F, col = e, xlim = c(1, n), ylim = c(1, n), pch = 20, xlab = "Species", ylab = "Sepals")
  par(new = T)

  dev.off()
}


# function for clustering two matrices
CreateCluster <- function(data, oldMeans){
  clusters = c()
  n = nrow(data)
  
  # cal diff and return min diff
  for (i in 1 : n){
    differences = c()
    k = nrow(oldMeans)

    for (j in 1 : k){
      di = data[i, ] - oldMeans[j, ]
      ds = sqrt(sum(di ** 2))
      differences = c(differences, ds)
    }

    minDiff = min(differences)
    cl = match(minDiff, differences)
    clusters = c(clusters, cl)
  }

  return (clusters)
}

# function for Euclidean distance
EuclideanDistance <- function(a, b){
  d = sqrt(a ** 2 + b ** 2);
}

# function to update the mean of the cluster
UpdateMean <- function(data, cluster, n){
  means = c()
  for (c in 1 : n){
    # get the point of cluster
    group = which(cluster == c)

    # compute mean point 
    mt1 = mean(data[group, 1])
    mt2 = mean(data[group, 2])
    vMean = c(mt1, mt2)
    means = c(means, vMean)
  }

  newM = matrix(means, ncol = 2, byrow = TRUE)
  return (newM)
}

# function delta to cal the E dist
Delta <- function(oldMeans, newMeans){
  a = newMeans - oldMeans
  return (max(EuclideanDistance(a[ , 1], a[ , 2])))
}

########################################################
# data preprocessing, selecting only first two col
# since it will be 2D array
x = iris[, c(1, 2)]
y = iris$Species

# saving a plot
# dev.new()
# plotTitle = paste("K-Means Clustering K = ", NOP)
# plot(x, xlim = c(1,max(x)), ylim = c(1,max(x)),
#     col = y, 
#     xlab = "Sepals", ylab = "Species",
#     pch = 20, main = plotTitle)

KMeansClustering(x, 10)