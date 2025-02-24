import { View, Text, ActivityIndicator, TouchableOpacity } from "react-native";
import MyStyle from "../../Style/MyStyle"; // ✅ Đã sửa lỗi tên biến
import style from "./style"; // ✅ Đổi từ Styles -> style
import { useEffect, useState } from "react";
import { endpoints, authAPI } from "../../Configs/API";
import { ScrollView } from "react-native-gesture-handler";
import { Chip } from "react-native-paper"; // ✅ Thêm import Chip nếu chưa có

const Home = () => {
    const [courses, setCourses] = useState(null);

    useEffect(() => {
        const loadCourses = async () => {
            try {
                let res = await authAPI.get(endpoints.courses); // ✅ Đã sửa
                setCourses(res.data.results);
            } catch (error) {
                console.error("Lỗi tải courses:", error);
            }
        };
        loadCourses();
    }, []);

    return (
        <View style={MyStyle.container}>
            <Text style={style.subject}>HOME</Text>  {/* ✅ Sửa Styles -> style */}
            <ScrollView style={{ flex: 1, flexDirection: "row" }}>
                {courses === null ? <ActivityIndicator /> : (
                    courses.map(c => (
                        <View key={c.id}>
                             <TouchableOpacity key={c.id} onPress={() => search(c.id)}>
                                <Chip icon="label" style={style.margin}>{c.name}</Chip>  {/* ✅ Sửa Styles -> style */}
                            </TouchableOpacity>
                        </View>
                    ))
                )}
            </ScrollView>
        </View>
    );
}; 

export default Home;
