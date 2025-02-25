import { View, Text, ActivityIndicator, TouchableOpacity, Image, FlatList } from "react-native";
import MyStyle from "../../Style/MyStyle";
import style from "./style";
import { useEffect, useState } from "react";
import { endpoints, authAPI } from "../../Configs/API";
import { Chip } from "react-native-paper";

const Home = () => {
  const [courses, setCourses] = useState(null);

  useEffect(() => {
    const loadCourses = async () => {
      try {
        let res = await authAPI.get(endpoints.courses);
        setCourses(res.data.results);
      } catch (error) {
        console.error("Lỗi tải courses:", error);
      }
    };
    loadCourses();
  }, []);

  return (
    <View style={MyStyle.container}>
      <Text style={style.subject}>HOME</Text>

      {courses === null ? (
        <ActivityIndicator />
      ) : (
        <FlatList
          data={courses}
          keyExtractor={(item) => item.id.toString()}
          renderItem={({ item }) => (
            <View style={{ margin: 10 }}>
              <Image
                source={{ uri: item.image }}
                style={{ width: 150, height: 100, borderRadius: 10 }}
              />
              <TouchableOpacity onPress={() => search(item.id)}>
                <Chip icon="label">{item.subject}</Chip>
              </TouchableOpacity>
            </View>
          )}
          contentContainerStyle={{ paddingBottom: 20 }}
        />
      )}
    </View>
  );
};

export default Home;
