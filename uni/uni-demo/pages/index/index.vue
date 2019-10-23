import AppUrl from './api/base_api.js'

<template>
	<view class="container">
		<view class="container_search">
			<view class="search_button">
				<image class="search_button_img" src="../../static/logo.png"> 杭州</image>
				
			</button>
		</view>
		<view class="container_swiper">
			<swiper  class="swiper-style" :indicator-dots="indicatorDots" autoplay="autoplay" :interval="interval" :duration="duration">
				<swiper-item v-for="(item , index) in banner_index" :key="index">
					<image class="swiper-style-item" :src="item.img" mode="scaleToFill" @click="onItemClick(item)"></image>
				</swiper-item>
			</swiper>
			<view class="line"></view>
		</view>
		
		
	</view>
	
</template>

<script>
	import AppUrl from '../../api/baseApi.js'
	export default {
		data() {
			return {
				indicatorDots: true,
				autoplay: true,
				interval: 2000,
				duration: 500,
				"banner_index": [{
					"img": "",
					"type": "",
					"param": ""
				}],
			}
		},
		onLoad() {
			var _self = this;
			const requestTask1 = uni.request({
				url: AppUrl.HOME_INDEX,
				success: (res) => {
					_self.banner_index = res.data.data.banner_index;

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
						})
						break;
					default:
						break;
				}

			}
		}
	}
</script>

<style>
	.container{
		display: flex;
		flex-direction:column; 
		width: 100%;
	
	}
	.line{
		width: 15px;
	}
	.container_seach{
		display: flex;
		flex-direction: row;
		width: 100%;
	}
	.search_button{
		display: flex;
		flex-direction: row;
		align-items: center;
		justify-content: center;
		width: 50px;
		height: 50px;
		box-shadow: none;
		
	}
	.search_button_img{
		width: 10px;
		height: 10px;
	}
	.container_swiper{
		display: flex;
		flex-direction: row;
		width: 100%;
	}
	.swiper-style {
		width: 100%;
		height: 160px;
	    margin: 30rpx 0rpx 0rpx 30rpx;
	}

	.swiper-style-item {
		justify-content: center;
		width: 100%;
		height: 160px;
		
	}
</style>
