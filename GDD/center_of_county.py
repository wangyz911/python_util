# import geopandas as gpd
#
# # 加载Shapefile文件
# counties = gpd.read_file("China2023County.shp")
#
# # 计算质心
# counties_centroids = counties.centroid
#
# # 创建一个新的GeoDataFrame，包含原始数据和质心坐标
# counties_with_centroids = counties.copy()
# counties_with_centroids['centroid'] = counties_centroids

import geopandas as gpd

# 加载Shapefile文件
counties = gpd.read_file("map2023/China2023County.shp")

# 检查原始CRS
print("Original CRS:", counties.crs)

# 将几何数据投影到一个平面CRS中，例如使用世界墨卡托投影（EPSG:3395）
counties_projected = counties.to_crs(epsg=3395)

# 在投影后的数据上计算质心
counties_centroids = counties_projected.centroid
counties_centroids = counties_centroids.to_crs(counties.crs)
# # 创建一个新的GeoDataFrame，包含原始数据和质心坐标
counties_with_centroids = counties.copy()
counties_with_centroids['centroid'] = counties_centroids.to_crs(counties.crs)

# 需要先将GeoSeries转换为字符串，以便正确保存到Excel中
counties_with_centroids['centroid'] = counties_with_centroids['centroid'].apply(lambda x: f"{x.x}, {x.y}")

# 保存为Excel文件
counties_with_centroids.to_csv("map2023/China2023CountyCentroids_crs.csv", index=False)



