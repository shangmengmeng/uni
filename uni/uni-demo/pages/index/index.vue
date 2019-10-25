import AppUrl from './api/base_api.js'

<template>
	<view class="container">
		<view style="width: 90%; display: flex;flex-direction: column;">
			<view class="container_search">
				<view class="search_button" @click="onCityClick">
					<image class="search_button_img" src="../../static/logo.png"></image>
					<label class="search_button_lab" font-size="12sp">{{ currentCity }}</label>
				</view>
				<view class="search_button_view" @click="onSearchClick">
					<image style="height: 10px; width: 10px;" src="../../static/main_find.png"></image>
					<label style="height: auto;width: auto; font-size: 14rpx; color: #999999;margin-left: 10rpx;">搜索相关信息...</label>
				</view>
			</view>
			<view class="container_swiper">
				<swiper class="swiper-style" :indicator-dots="indicatorDots" autoplay="autoplay" :interval="interval" :duration="duration">
					<swiper-item v-for="(item, index) in banner_index" :key="index">
						<image class="swiper-style-item" :src="item.img" mode="scaleToFill" @click="onItemClick(item)"></image>
					</swiper-item>
				</swiper>
			</view>
			<view style="display: flex;flex-direction: row;width: 100%;height: 150rpx; margin-top: 15rpx; align-items: center;justify-content: center;">
				<view
					style=" width:100%;height:150rpx;fledisplay: flex;flex-direction: column;  margin: 5rpx;justify-content: center;"
					v-for="(item, index) in board_model"
					:key="index"
					@click="onBoardItemClick(index)"
				>
					<view style="display: flex;flex-direction: column; align-items: center;">
						<image style="width: 80rpx; height: 80rpx;" :src="item.imgSrc" mode="aspectFit"></image>
						<label style="font-size: 25rpx; width: 80rpx; height: 20rpx; text-align: center;padding-top: 15rpx;">{{ item.name }}</label>
					</view>
				</view>
			</view>
			<view class="port">
				<view style="width: 100%; height: 50px; display: flex;flex-direction: row; align-items: center; margin-top: 15rpx">
					<view style="background: #4CD964; width: 4px; height: 25rpx;"></view>
					<label style="flex:0.5;padding-left: 20rpx; font-size: 26rpx; color: #333333;text-align: left|center;font-weight: bold;">大宗专供</label>
					<label style="flex:0.4;text-align: right; font-size: 22rpx;">查看更多 >></label>
				</view>
				<scroll-view style="width: 100%;height: 200rpx;display: flex; flex-direction: row; margin-left: 30rxp;" scroll-x="true">
					<view v-for="(item, index) in agshop_wharf" :key="index" @click="onPortItemClick(index)" style="padding-left: 30rpx;">
						<view style="width: 280rpx; height: 250rpx; display: flex; flex-direction: column; align-content: flex-end;">
							
							<image style="width: 100%; height: 250px; z-index: -1;" :src="item.imgsarr[0]" mode="scaleToFill"></image>
							<view style="width: 100%; height: -100rpx; margin-bottom: 100rpx; background: rgb(23,200,230,0.1); text-align: center; z-index: 1;">我来了</view>
						</view>
					</view>
				</scroll-view>
			</view>
		</view>
	</view>
</template>

<script>
import AppUrl from '../../api/baseApi.js';
export default {
	data() {
		return {
			currentCity: '',
			board_model: [
				{ imgSrc: '../../static/icon_1.png', name: '资讯' },
				{ imgSrc: '../../static/icon_2.png', name: '集采' },
				{ imgSrc: '../../static/icon_3.png', name: '设备' },
				{ imgSrc: '../../static/icon_4.png', name: '供需' },
				{ imgSrc: '../../static/icon_5.png', name: '价格' }
			],
			indicatorDots: true,
			autoplay: true,
			interval: 2000,
			duration: 500,
			banner_index: [
				{
					img: '',
					type: '',
					param: ''
				}
			],
			agshop_wharf: [
				{
					id: '',
					type: 1,
					name: '',
					imgs: '',
					d_depth: '',
					b_tonnage: '',
					localtion: '',
					address: '',
					server_shipping: 2,
					server_towharf: '',
					server_loading: '',
					server_range: '',
					server_lgtype: '',
					intro: '',
					state: 2,
					created_at: '',
					updated_at: '',
					imgsarr: ['', '']
				}
			]
		};
	},
	onLoad() {
		var _self = this;
		let params = '';
		//uni获取经纬度
		uni.getLocation({
			//type: 'wgs84',
			success: function(res) {
				params = res;
				// 高德地图web逆向编码获取定位
				uni.request({
					url: 'https://restapi.amap.com/v3/geocode/regeo?key=5950e290e01ff9b7c43ec0508f5afe72&location=' + params.longitude + ',' + params.latitude,
					success: res => {
						_self.currentCity = res.data.regeocode.addressComponent.city;
					}
				});
			}
		});
		const requestTask1 = uni.request({
			url: AppUrl.HOME_INDEX,
			success: res => {
				_self.banner_index = res.data.data.banner_index;
				_self.agshop_wharf = res.data.data.agshop_wharf;
			}
		});
	},
	methods: {
		onItemClick: function(options) {
			switch (options.type) {
				case 'report': //跳转到数据模块
					break;
				case 'aggongxu':
					break;
				case 'report': //跳转到供需主页
					break;
				case 'h5': //跳转到活动页面
					uni.navigateTo({
						url: '../web/common-webview/common-webview?webUrl=' + options.param
					});
					break;
				default:
					break;
			}
		},
		onCityClick: function() {
			uni.showToast({
				title: '我被点击了获取城市'
			});
		},
		onSearchClick: function() {
			uni.showToast({
				title: '我被点击了搜索'
			});
		},
		onBoardItemClick: function(options) {
			uni.showToast({
				title: options
			});
		},
		onPortItemClick: function(options) {
			uni.showToast({
				title: options
			});
		}
	}
};
</script>

<style>
.container {
	display: flex;
	flex-direction: column;
	width: 100%;
	align-items: center;
}

/* 搜索栏 */
.container_search {
	display: flex;
	flex-direction: row;
	align-items: center;
	width: 100%;
}

.search_button {
	display: flex;
	flex-direction: row;
	align-items: center;
	justify-content: flex-start;
	width: 70px;
	height: 50px;
}

.search_button_img {
	width: 10px;
	height: 10px;
	font-size: 5px;
}

.search_button_lab {
	font-size: 12px;
	color: #007aff;
	padding-left: 15rpx;
}
.search_button_view {
	margin-left: 30rpx;
	border-radius: 50rpx;
	baseline-shift: baseline;
	width: 420rpx;
	height: 50rpx;
	display: flex;
	flex-direction: row;
	align-items: center;
	justify-content: center;
	background: #f1f5f8;
}

.container_swiper {
	display: flex;
	flex-direction: row;
	width: 100%;
}

.swiper-style {
	border-radius: 15rpx;
	width: 100%;
	height: 160px;
}

.swiper-style-item {
	justify-content: center;
	width: 100%;
	height: 160px;
}
.port {
	display: flex;
	flex-direction: column;
	width: 100%;
	height: 280rpx;
}
</style>
