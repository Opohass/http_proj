from pandas.api.types import is_numeric_dtype

class MinMaxScale:
    def __init__(self) -> None:
        self.X_min=None
        self.X_max=None

    def fit(self,x):
        x.replace({False: 0, True: 1}, inplace=True) #converting any boolean column to numerical
        #checking if all the features are numerical
        for i in x:
            if not is_numeric_dtype(x[i]):
                raise ValueError(f"column '{i}' is not numeric")

        self.X_min=x.min(axis=0)
        self.X_max=x.max(axis=0)

    def transform(self,x): 
        if self.X_min is None or self.X_max is None:
            raise TypeError("model was not fitted before transformation")

        x.replace({False: 0, True: 1}, inplace=True) #converting any boolean column to numerical
        X_std = (x-self.X_min)/(self.X_max-self.X_min)
        
        #if both max and min of a column are 0 then it would devide by 0 and will return nan.
        #we are changing these columns to 0
        maxs=self.X_max[self.X_max==0].index
        mins=self.X_min[self.X_min==0].index
        X_std[(mins) & (maxs)]=0
        return X_std

    def fit_transform(self,x):
        self.fit(x)
        return self.transform(x)