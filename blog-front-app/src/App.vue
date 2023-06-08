<template>
  <div>
    <form @submit.prevent="submitForm">
      <label for="email">Email:</label>
      <input id="email" v-model="user.email" type="email" />

      <label for="username">Username:</label>
      <input id="username" v-model="user.username" type="text" />

      <label for="password">Password:</label>
      <input id="password" v-model="user.password" type="password" />

      <input type="submit" value="Submit">

      <!-- Message -->
      <div v-if="message">
        {{ message }}
      </div>
    </form>
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue'
import axios from 'axios'

interface User {
  email: string;
  username: string;
  password: string;
}

interface AxiosError {
  message: string;
  response?: {
    status: number;
    headers: any;
    data: any;
  };
  request?: any;
  config: any;
}

const users = ref<User[]>([]);
const user = ref<User>({ email: '', username: '', password: '' });
const message = ref('');

const submitForm = async () => {
  message.value = '';
  try {
    const response = await axios.post('http://localhost:8000/api/users/', user.value)
    message.value = 'User created successfully!';
  } catch (error: any) {
    if (error.response) {
      switch (error.response.status) {
        case 400:
          message.value = '잘못된 요청입니다. 입력 내용을 확인해주세요.';
          break;
        case 404:
          message.value = '리소스를 찾을 수 없습니다.';
          break;
        default:
          message.value = '오류가 발생했습니다.';
      }
    } else {
      message.value = '서버가 응답하지 않았습니다.';
    }
  }
}
</script>